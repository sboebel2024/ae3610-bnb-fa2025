import pandas as pd
import os

# === INPUT AND OUTPUT FILES ===
input_file = "cantilever_disp_tests.csv"     
output_file = "cantilever_strain_disp.csv"  

# === READ DATA ===
df = pd.read_csv(input_file)

# === VERIFY REQUIRED COLUMNS ===
required_cols = ["Delta_in", "Avg_eA", "Avg_eB", "Avg_eC"]
if not all(col in df.columns for col in required_cols):
    raise ValueError("CSV must contain columns: Delta_in, Avg_eA, Avg_eB, and Avg_eC")

# === COMPUTE LOCAL STRAIN COMPONENTS ===
df["eps_x"] = df["Avg_eA"]                          
df["eps_y"] = df["Avg_eC"]                          
df["gamma_xy"] = 2 * (df["Avg_eB"] - 0.5 * (df["Avg_eA"] + df["Avg_eC"])) 

# === ORGANIZE OUTPT COLUMNS ===
output_cols = [
    "File", "Delta_in", "Avg_eA", "Avg_eB", "Avg_eC",
    "eps_x", "eps_y", "gamma_xy"
]
df_out = df[output_cols]

# === SAVE TO CSV ===
df_out.to_csv(output_file, index=False)

print(f"Strain vs. Displacement data saved to {output_file}")
print(df_out)