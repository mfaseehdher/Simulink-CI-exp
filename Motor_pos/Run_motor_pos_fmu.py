import numpy as np
import pandas as pd
from pathlib import Path
from fmpy import simulate_fmu, read_model_description

HERE = Path(__file__).resolve().parent
FMU = HERE / "Motor_pos.fmu"   # FIXED name

STOP = 3.0
DT = 0.001

def main():
    if not FMU.exists():
        raise FileNotFoundError(f"FMU not found: {FMU}")

    md = read_model_description(str(FMU))
    inputs = [v.name for v in md.modelVariables if v.causality == "input"]
    outputs = [v.name for v in md.modelVariables if v.causality == "output"]

    print("Inputs:", inputs)
    print("Outputs:", outputs)

    in_name = inputs[0]
    out_name = outputs[0]

    # Step input
    t = np.arange(0.0, STOP + DT, DT)
    u = np.zeros_like(t)
    u[t >= 0.2] = 1.0

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
    out_csv = HERE / "motor_pos_result.csv"
    df.to_csv(out_csv, index=False)

    print("Saved:", out_csv)

if __name__ == "__main__":
    main()
