import numpy as np
import pandas as pd
from pathlib import Path
from fmpy import simulate_fmu, read_model_description

HERE = Path(__file__).resolve().parent
FMU = HERE / "Motor_Model.fmu"

STOP = 3.0
DT = 0.001

# If your FMU uses different names, we auto-detect below.
PREFERRED_INPUT = "Voltage"
PREFERRED_OUTPUT = "Speed"

def detect_io_names(fmu_path: Path):
    md = read_model_description(str(fmu_path))
    inputs = [v.name for v in md.modelVariables if v.causality == "input"]
    outputs = [v.name for v in md.modelVariables if v.causality == "output"]

    # choose preferred if present; else fall back to first available
    in_name = PREFERRED_INPUT if PREFERRED_INPUT in inputs else (inputs[0] if inputs else None)
    out_name = PREFERRED_OUTPUT if PREFERRED_OUTPUT in outputs else (outputs[0] if outputs else None)

    return in_name, out_name, inputs, outputs

def main():
    if not FMU.exists():
        raise FileNotFoundError(f"FMU not found: {FMU}")

    in_name, out_name, inputs, outputs = detect_io_names(FMU)

    print("FMU:", FMU)
    print("Inputs found:", inputs)
    print("Outputs found:", outputs)

    if in_name is None:
        raise RuntimeError("No input variables found in FMU. Check your Simulink Inport / FMU export.")
    if out_name is None:
        raise RuntimeError("No output variables found in FMU. Check your Simulink Outport / FMU export.")

    print(f"Using input: {in_name}")
    print(f"Using output: {out_name}")

    # Step voltage: 0 -> 12V at t = 0.2s
    t = np.arange(0.0, STOP + DT, DT)
    u = np.zeros_like(t)
    u[t >= 0.2] = 12.0

    inp = np.zeros(len(t), dtype=[("time", np.float64), (in_name, np.float64)])
    inp["time"] = t
    inp[in_name] = u

    # Default parameters (same names you found: J, K, L, R, b)
    start_values = {"J": 0.01, "K": 0.01, "L": 0.5, "R": 1.0, "b": 0.1}

    result = simulate_fmu(
        str(FMU),
        input=inp,
        start_values=start_values,
        stop_time=STOP,
        output=[out_name],  # ensure the output is included
    )

    df = pd.DataFrame(result)

    # Save CSV
    out_csv = HERE / "motor_speed_result.csv"
    df.to_csv(out_csv, index=False)
    print("Saved:", out_csv)

if __name__ == "__main__":
    main()
