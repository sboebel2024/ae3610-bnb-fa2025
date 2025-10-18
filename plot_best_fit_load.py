import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

input_file = "rosette_local_strains_load.csv"
output_plot = "eps1_vs_load_bw.png"

df = pd.read_csv(input_file)
df["Load_N"] = df["Load_g"] * 9.81e-3
df["eps_1"] = 0.5 * (df["eps_x"] + df["eps_y"]) + (
    ((0.5 * (df["eps_x"] - df["eps_y"]))**2 + (0.5 * df["gamma_xy"])**2) ** 0.5
)

x = df["Load_N"]
y = df["eps_1"]

m, b = np.polyfit(x, y, 1)
y_fit = m * x + b
r2 = 1 - np.sum((y - y_fit)**2) / np.sum((y - np.mean(y))**2)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'ko', label=r"$\varepsilon_1$ data")
plt.plot(x, y_fit, 'k--', label=f"y = {m:.2f}x + {b:.2f}\nR² = {r2:.4f}")
plt.xlabel("Load (N)", fontsize=12)
plt.ylabel(r"$\varepsilon_1$ (µε)", fontsize=12)
plt.grid(True, linestyle='--', color='0.7', alpha=0.8)
plt.legend()
plt.tight_layout()
plt.savefig(output_plot, dpi=300, bbox_inches="tight")
print(f"Plot with best-fit line and R² saved as {output_plot}")

plt.show()