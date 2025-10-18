import pandas as pd
import matplotlib.pyplot as plt

input_file = "rosette_local_strains_load.csv"  
output_plot = "strain_vs_load.png"

df = pd.read_csv(input_file)

df = pd.read_csv(input_file)
df["Load_N"] = df["Load_g"] * 9.81e-3

plt.figure(figsize=(8, 6))
plt.plot(df["Load_N"], df["eps_x"], 'ko-', label=r"$\varepsilon_X^*$")
plt.plot(df["Load_N"], df["eps_y"], 'k--s', label=r"$\varepsilon_Y^*$")
plt.plot(df["Load_N"], df["gamma_xy"], 'k:^', label=r"$\gamma_{XY}^*$")

plt.xlabel("Applied Load (N)", fontsize=12)
plt.ylabel("Strain (µε)", fontsize=12)
plt.grid(True, linestyle='--', color='0.7', alpha=0.8)
plt.legend()
plt.tight_layout()
plt.savefig(output_plot, dpi=300, bbox_inches="tight")
print(f"Black & white combined plot saved as {output_plot}")
plt.show()