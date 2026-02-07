import pandas as pd
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
CSV = HERE / "motor_pos_result.csv"

def main():
    df = pd.read_csv(CSV)

    time = "time"
    output = [c for c in df.columns if c != time][0]

    plt.figure()
    plt.plot(df[time], df[output])
    plt.xlabel("Time (s)")
    plt.ylabel(output)
    plt.title("Motor Position Response")
    plt.grid(True)

    out_png = HERE / "motor_pos_plot.png"
    plt.savefig(out_png, dpi=300)
    plt.close()

    print("Saved:", out_png)

if __name__ == "__main__":
    main()
