import pandas as pd
import matplotlib
matplotlib.use("Agg")  # required in CI (no display)
import matplotlib.pyplot as plt
from pathlib import Path

HERE = Path(__file__).resolve().parent
df = pd.read_csv(HERE / "motor_result.csv")

plt.figure()
plt.plot(df["time"], df["Speed"])
plt.xlabel("Time (s)")
plt.ylabel("Speed")
plt.title("Motor Speed Response")
plt.grid(True)
plt.savefig(HERE / "motor_plot.png", dpi=300)
plt.close()

print("Saved: motor_plot.png")
