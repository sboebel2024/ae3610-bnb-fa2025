import pandas as pd
import matplotlib.pyplot as plt

input_file = "rosette_local_strains_disp.csv"
output_plot = "strain_vs_deflection_bw.png"

df = pd.read_csv(input_file)
df["Delta_m"] = df["Delta_in"] * 0.0254

plt.figure(figsize=(8, 6))
plt.plot(df["Delta_m"], df["eps_x"], 'ko-', label=r"$\varepsilon_X^*$")
plt.plot(df["Delta_m"], df["eps_y"], 'k--s', label=r"$\varepsilon_Y^*$")
plt.plot(df["Delta_m"], df["gamma_xy"], 'k:^', label=r"$\gamma_{XY}^*$")

plt.xlabel("Applied Deflection (m)", fontsize=12)
plt.ylabel("Strain (µε)", fontsize=12)
plt.grid(True, linestyle='--', color='0.7', alpha=0.8)
plt.legend()
plt.tight_layout()
plt.savefig(output_plot, dpi=300, bbox_inches="tight")
print(f"Black & white plot saved as {output_plot}")
plt.show()
