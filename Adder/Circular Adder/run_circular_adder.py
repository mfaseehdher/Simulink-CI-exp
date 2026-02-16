    # y1(t) = u1(t) + y2(t-1)
    # y2(t) = u2(t) + y1(t)

import csv
from pathlib import Path

from fmpy import read_model_description, extract
from fmpy.fmi2 import FMU2Slave

FMU1_FILE = "adder.fmu"
FMU2_FILE = "adder1.fmu"
INPUT_CSV = "input_circular.csv"
OUTPUT_CSV = "output_circular.csv"

IN1 = "Inport"
IN2 = "Inport1"
OUT = "Outport"


CSV_U1 = "u1"   # external input to FMU1
CSV_U2 = "u2"   # external input to FMU2


DT = 0.1
START_TIME = 0.0


Y2_INIT = 0.0


def load_fmu(fmu_path: Path, instance_name: str):
    if not fmu_path.exists():
        raise FileNotFoundError(f"FMU not found: {fmu_path}")

    md = read_model_description(str(fmu_path))
    if md.coSimulation is None:
        raise RuntimeError(f"{fmu_path.name} is not FMI 2.0 Co-Simulation")

    vr = {v.name: v.valueReference for v in md.modelVariables}

    unzipdir = extract(str(fmu_path))
    fmu = FMU2Slave(
        guid=md.guid,
        unzipDirectory=unzipdir,
        modelIdentifier=md.coSimulation.modelIdentifier,
        instanceName=instance_name,
    )

    fmu.instantiate()
    fmu.setupExperiment(startTime=START_TIME)
    fmu.enterInitializationMode()
    fmu.exitInitializationMode()

    return fmu, vr


def main():
    base = Path(".")
    fmu1_path = base / FMU1_FILE
    fmu2_path = base / FMU2_FILE
    input_path = base / INPUT_CSV
    output_path = base / OUTPUT_CSV

    if not input_path.exists():
        raise FileNotFoundError(f"CSV not found: {input_path}")

    # Load FMUs
    fmu1, vr1 = load_fmu(fmu1_path, "adder_instance_1")
    fmu2, vr2 = load_fmu(fmu2_path, "adder_instance_2")

    # Validate variable names exist
    for name in [IN1, IN2, OUT]:
        if name not in vr1:
            raise KeyError(f"Variable '{name}' not found in {FMU1_FILE}")
        if name not in vr2:
            raise KeyError(f"Variable '{name}' not found in {FMU2_FILE}")

    # Read CSV
    with input_path.open(newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        headers = reader.fieldnames or []

    for col in [CSV_U1, CSV_U2]:
        if col not in headers:
            raise KeyError(
                f"CSV column '{col}' missing. Expected header: {CSV_U1},{CSV_U2}"
            )


    t = START_TIME
    y2_prev = Y2_INIT
    results = []

    for row in rows:
        u1 = float(row[CSV_U1])
        u2 = float(row[CSV_U2])

        # FMU1: y1 = u1 + y2_prev
        fmu1.setReal([vr1[IN1], vr1[IN2]], [u1, y2_prev])
        fmu1.doStep(currentCommunicationPoint=t, communicationStepSize=DT)
        y1 = fmu1.getReal([vr1[OUT]])[0]

        # FMU2: y2 = u2 + y1
        fmu2.setReal([vr2[IN1], vr2[IN2]], [u2, y1])
        fmu2.doStep(currentCommunicationPoint=t, communicationStepSize=DT)
        y2 = fmu2.getReal([vr2[OUT]])[0]

        # Update feedback for next step (the "delay")
        y2_prev = y2

        results.append((t, u1, u2, y1, y2))
        t = round(t + DT, 12)

    # Terminate
    for fmu in (fmu1, fmu2):
        fmu.terminate()
        fmu.freeInstance()

    # Write output
    with output_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["time", "u1", "u2", "y1(FMU1)", "y2(FMU2)"])
        w.writerows(results)

    print("✅ Circular FMU coupling finished")
    print(f"Output written to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
