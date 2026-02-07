import numpy as np
import pandas as pd
from pathlib import Path
from fmpy import simulate_fmu, read_model_description

HERE = Path(__file__).resolve().parent
FMU = HERE / "Motor_Model.fmu"

STOP = 3.0
DT = 0.001

def main():
    if not FMU.exists():
        raise FileNotFoundError(f"FMU not found: {FMU}")

    md = read_model_description(str(FMU))
    inputs = [v.name for v in md.modelVariables if v.causality == "input"]
    outputs = [v.name for v in md.modelVariables if v.causality == "output"]

    print("FMU:", FMU)
    print("Inputs found:", inputs)
    print("Outputs found:", outputs)

    if not inputs or not outputs:
        raise RuntimeError("FMU must have at least one input and one output.")

    in_name = inputs[0]    # In1
    out_name = outputs[0]  # Out1

    print(f"Using input: {in_name}")
    print(f"Using output: {out_name}")

    # Step input: 0 -> 12 at t=0.2s
    t = np.arange(0.0, STOP + DT, DT)
    u = np.zeros_like(t)
    u[t >= 0.2] = 12.0

    inp = np.zeros(len(t), dtype=[("time", np.float64), (in_name, np.float64)])
    inp["time"] = t
    inp[in_name] = u

    result = simulate_fmu(
        str(FMU),
        input=inp,
        stop_time=STOP,
        output=[out_name],
    )

    df = pd.DataFrame(result)
    out_csv = HERE / "motor_speed_result.csv"
    df.to_csv(out_csv, index=False)
    print("Saved:", out_csv)

if __name__ == "__main__":
    main()
