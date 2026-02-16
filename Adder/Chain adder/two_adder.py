    # FMU1: sum1 = a + b
    # FMU2: sum2 = sum1 + c

import csv
from pathlib import Path

from fmpy import read_model_description, extract
from fmpy.fmi2 import FMU2Slave



FMU1_FILE = "adder.fmu"
FMU2_FILE = "adder1.fmu"
INPUT_CSV = "input_noncircular.csv"
OUTPUT_CSV = "output_chain.csv"


IN_A = "Inport"
IN_B = "Inport1"
OUT_Y = "Outport"

CSV_C = "c"


DT = 0.1
START_TIME = 0.0


def load_fmu(fmu_path: Path, instance_name: str):
    """Load FMI 2.0 Co-Simulation FMU -> returns (fmu_instance, vr_map, model_description)."""
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

    # FMI init sequence
    fmu.instantiate()
    fmu.setupExperiment(startTime=START_TIME)
    fmu.enterInitializationMode()
    fmu.exitInitializationMode()

    return fmu, vr, md


def main():
    base = Path(".")
    fmu1_path = base / FMU1_FILE
    fmu2_path = base / FMU2_FILE
    input_path = base / INPUT_CSV
    output_path = base / OUTPUT_CSV

    if not input_path.exists():
        raise FileNotFoundError(f"CSV not found: {input_path}")

    # Load both FMUs (can be identical models; instances must be different)
    fmu1, vr1, _ = load_fmu(fmu1_path, "adder_instance_1")
    fmu2, vr2, _ = load_fmu(fmu2_path, "adder_instance_2")

    # Validate required variable names exist in BOTH FMUs
    for name in [IN_A, IN_B, OUT_Y]:
        if name not in vr1:
            raise KeyError(f"Variable '{name}' not found in {FMU1_FILE}")
        if name not in vr2:
            raise KeyError(f"Variable '{name}' not found in {FMU2_FILE}")

    # Read all CSV rows into memory
    with input_path.open(newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        headers = reader.fieldnames or []

    # Validate CSV headers
    for col in [IN_A, IN_B, CSV_C]:
        if col not in headers:
            raise KeyError(
                f"CSV column '{col}' missing. Expected header to include: {IN_A}, {IN_B}, {CSV_C}"
            )

    t = START_TIME
    results = []

    for row in rows:
        a = float(row[IN_A])
        b = float(row[IN_B])
        c = float(row[CSV_C])

        # ---- FMU 1 ----
        fmu1.setReal([vr1[IN_A], vr1[IN_B]], [a, b])
        fmu1.doStep(currentCommunicationPoint=t, communicationStepSize=DT)
        sum1 = fmu1.getReal([vr1[OUT_Y]])[0]

        # ---- FMU 2 ----
        # Feed FMU1 output into FMU2 input
        fmu2.setReal([vr2[IN_A], vr2[IN_B]], [sum1, c])
        fmu2.doStep(currentCommunicationPoint=t, communicationStepSize=DT)
        sum2 = fmu2.getReal([vr2[OUT_Y]])[0]

        results.append((t, a, b, c, sum1, sum2))
        t = round(t + DT, 12)

    # Terminate FMUs cleanly
    for fmu in (fmu1, fmu2):
        fmu.terminate()
        fmu.freeInstance()

    # Write output CSV
    with output_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["time", "a(Inport)", "b(Inport1)", "c(CSV)", "sum1(FMU1)", "sum2(FMU2)"])
        w.writerows(results)

    print("✅ Two-adder non-circular FMU chain finished")
    print(f"Output written to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
