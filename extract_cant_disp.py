import os
import pandas as pd

folder = "A_8Y_export"

extractions = [
    (1200, 1400, 0.1),
    (1700, 1900, 0.2),
    (2100, 2200, 0.3),
    (2500, 2700, 0.4),
    (2900, 3100, 0.5), 
    (3400, 3500, 0.6)
]

file_name = "Session #6.csv"
file_path = os.path.join(folder, file_name)

if not os.path.exists(file_path):
    raise FileNotFoundError(f"⚠️ File not found: {file_name}")

df = pd.read_csv(file_path)
if not all(col in df.columns for col in ["time", "eA", "eB", "eC"]):
    raise ValueError(f"⚠️ Missing expected columns in {file_name}")

results = []

for (start, end, delta) in extractions:
    start, end = sorted((start, end))
    
    subset = df[(df["time"] >= start) & (df["time"] <= end)]
    if subset.empty:
        print(f"⚠️ No data found for {start}-{end}")
        continue

    avg_eA = subset["eA"].mean()
    avg_eB = subset["eB"].mean()
    avg_eC = subset["eC"].mean()

    results.append({
        "File": file_name,
        "Delta_in": delta,
        "Time_Start": start,
        "Time_End": end,
        "Avg_eA": avg_eA,
        "Avg_eB": avg_eB,
        "Avg_eC": avg_eC
    })

output_df = pd.DataFrame(results)
output_file = "averages_session6.csv"
output_df.to_csv(output_file, index=False)

print(f"Averages for Session #6 successfully saved to {output_file}")
