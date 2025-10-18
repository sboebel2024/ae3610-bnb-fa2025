import pandas as pd
import os

# === INPUT CSV FILE ===
input_file = "cantilever_load_tests.csv"  
output_file = "rosette_local_strains.csv"

# === Read Input Data ===
df = pd.read_csv(input_file)

# === Compute Local Strain Components ===
df["eps_x"] = df["Avg_eA"]
df["eps_y"] = df["Avg_eC"]
df["gamma_xy"] = 2 * (df["Avg_eB"] - 0.5 * (df["Avg_eA"] + df["Avg_eC"]))

# === Save to CSV ===
df.to_csv(output_file, index=False)

print(f"✅ Inferred local strains saved to {output_file}")
print(df[["File", "Load_g", "eps_x", "eps_y", "gamma_xy"]])