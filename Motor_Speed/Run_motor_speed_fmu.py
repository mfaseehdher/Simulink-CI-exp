import numpy as np
import pandas as pd
from pathlib import Path
from fmpy import simulate_fmu

HERE = Path(__file__).resolve().parent
FMU = HERE / "Motor_Model.fmu"

STOP = 3.0
DT = 0.001

INPUT_NAME = "Voltage"
OUTPUT_NAME = "Speed"

# Step input: 0 -> 12V at t=0.2s
t = np.arange(0.0, STOP + DT, DT)
u = np.zeros_like(t)
u[t >= 0.2] = 12.0

inp = np.zeros(len(t), dtype=[("time", np.float64), (INPUT_NAME, np.float64)])
inp["time"] = t
inp[INPUT_NAME] = u

# Default parameters (same as in Model Workspace)
start_values = {"J": 0.01, "K": 0.01, "L": 0.5, "R": 1.0, "b": 0.1}

print("Running FMU:", FMU)
result = simulate_fmu(str(FMU), input=inp, start_values=start_values)

df = pd.DataFrame(result)
out_csv = HERE / "motor_result.csv"
df.to_csv(out_csv, index=False)
print("Saved:", out_csv)
