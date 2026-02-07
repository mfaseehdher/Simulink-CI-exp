import pandas as pd
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # required in CI
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
CSV = HERE / "motor_speed_result.csv"

def main():
    if not CSV.exists():
        raise FileNotFoundError(f"CSV not found: {CSV}. Run Run_motor_speed_fmu.py first.")

    df = pd.read_csv(CSV)

    # Find output column (could be "Speed" or something else depending on FMU)
    # We assume time exists.
    time_col = "time"
    if time_col not in df.columns:
        raise RuntimeError(f"'time' column not found in CSV. Columns: {list(df.columns)}")

    # choose first non-time column as output
    out_cols = [c for c in df.columns if c != time_col]
    if not out_cols:
        raise RuntimeError("No output columns found in CSV (only time exists).")

    y_col = out_cols[0]

    plt.figure()
    plt.plot(df[time_col], df[y_col])
    plt.xlabel("Time (s)")
    plt.ylabel(y_col)
    plt.title("Motor response")
    plt.grid(True)

    out_png = HERE / "motor_speed_plot.png"
    plt.savefig(out_png, dpi=300)
    plt.close()
    print("Saved:", out_png)

if __name__ == "__main__":
    main()
