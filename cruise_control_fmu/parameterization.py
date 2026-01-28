import numpy as np
import pandas as pd
from fmpy import simulate_fmu

# FMU file
FMU = "ccmodel.fmu"

# Simulation settings
STOP = 120.0
DT = 0.01
INPUT_NAME = "In1"     # confirmed
OUTPUT_NAME = "Out1"
U_VALUE = 500.0

# Parameter cases: (m, b)
CASES = [
    (1000.0, 50.0),
    (2000.0, 50.0),
    (1000.0, 100.0),
]

# Build constant input u(t)
t = np.arange(0.0, STOP + DT, DT)
u = np.full_like(t, U_VALUE, dtype=float)

inp = np.zeros(len(t), dtype=[("time", np.float64), (INPUT_NAME, np.float64)])
inp["time"] = t
inp[INPUT_NAME] = u

# Run each case separately
for (m, b) in CASES:
    print(f"Running FMU with m={m}, b={b}")

    result = simulate_fmu(
        FMU,
        input=inp,
        start_values={
            "m": float(m),
            "b": float(b),
        },
    )

    df = pd.DataFrame(result)

    # Add parameters as columns (important for later plotting)
    df["m"] = float(m)
    df["b"] = float(b)
    df["u"] = float(U_VALUE)

    filename = f"result_m{int(m)}_b{int(b)}_u{int(U_VALUE)}.csv"
    df.to_csv(filename, index=False)

    print(f"Saved {filename}")

print("All CSV files generated successfully.")
