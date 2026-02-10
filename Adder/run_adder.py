"""
run_adder.py

Explicit FMI 2.0 Co-Simulation master for a simple Adder FMU.

What this script does:
- Reads inputs from input.csv (columns must match FMU input names)
- For each row:
    setReal -> doStep -> getReal
- Logs outputs to output.csv

Required files in the same folder:
- adder.fmu
- input.csv
- run_adder.py

Install dependency:
    pip install fmpy

Run:
    python run_adder.py
"""

import csv
from pathlib import Path

from fmpy import read_model_description, extract
from fmpy.fmi2 import FMU2Slave


# -------- File names --------
FMU_FILE = "adder.fmu"
INPUT_CSV = "input.csv"
OUTPUT_CSV = "output.csv"

# -------- FMU variable names (must match Simulink Inport/Outport names) --------
IN1_NAME = "Inport"
IN2_NAME = "Inport1"
OUT_NAME = "Outport"

# -------- Simulation settings --------
DT = 0.1
START_TIME = 0.0


def main():
    fmu_path = Path(FMU_FILE)
    input_path = Path(INPUT_CSV)
    output_path = Path(OUTPUT_CSV)

    if not fmu_path.exists():
        raise FileNotFoundError(f"FMU not found: {fmu_path}")
    if not input_path.exists():
        raise FileNotFoundError(f"CSV not found: {input_path}")

    # Read FMU model description
    model_description = read_model_description(str(fmu_path))
    if model_description.coSimulation is None:
        raise RuntimeError("This FMU is not FMI 2.0 Co-Simulation")

    # Map variable names to value references
    vr = {v.name: v.valueReference for v in model_description.modelVariables}

    # Check required variables exist
    for name in [IN1_NAME, IN2_NAME, OUT_NAME]:
        if name not in vr:
            raise KeyError(f"Variable '{name}' not found in FMU")

    # Extract and instantiate FMU
    unzipdir = extract(str(fmu_path))
    fmu = FMU2Slave(
        guid=model_description.guid,
        unzipDirectory=unzipdir,
        modelIdentifier=model_description.coSimulation.modelIdentifier,
        instanceName="adder_instance",
    )

    # FMI initialization
    fmu.instantiate()
    fmu.setupExperiment(startTime=START_TIME)
    fmu.enterInitializationMode()
    fmu.exitInitializationMode()

    # Read input CSV
    with input_path.open(newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Master loop
    time = START_TIME
    results = []

    for row in rows:
        u1 = float(row[IN1_NAME])
        u2 = float(row[IN2_NAME])

        # Set inputs
        fmu.setReal(
            [vr[IN1_NAME], vr[IN2_NAME]],
            [u1, u2]
        )

        # Advance one step
        fmu.doStep(
            currentCommunicationPoint=time,
            communicationStepSize=DT
        )

        # Get output
        y = fmu.getReal([vr[OUT_NAME]])[0]

        results.append((time, u1, u2, y))
        time = round(time + DT, 12)

    # Terminate FMU
    fmu.terminate()
    fmu.freeInstance()

    # Write output CSV
    with output_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time", IN1_NAME, IN2_NAME, OUT_NAME])
        writer.writerows(results)

    print("✅ Simulation finished")
    print(f"Output written to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
