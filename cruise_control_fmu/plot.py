import pandas as pd
import matplotlib.pyplot as plt
import os
print("Plot script running in:", os.getcwd())
print("Files available here:", os.listdir("."))

files = [
    "result_m1000_b50_u500.csv",
    "result_m2000_b50_u500.csv",
    "result_m1000_b100_u500.csv",
]

plt.figure()

for file in files:
    df = pd.read_csv(file)

    # Extract parameters from the file itself
    m = int(df["m"].iloc[0])
    b = int(df["b"].iloc[0])

    plt.plot(df["time"], df["Out1"], label=f"m={m}, b={b}")

plt.xlabel("Time (s)")
plt.ylabel("V")
plt.title("Parameters comparision")
plt.grid(True)
plt.legend()
plt.savefig("combined_parameter_plot.png", dpi=300)
print("Plot saved as combined_parameter_plot.png")


