import os
import pandas as pd

folder = "A_8Y_export"

extractions = {
    "Session #2.csv": [(750, 1500, 200)],
    "Session #3.csv": [(300, 500, 400)],
    "Session #4.csv": [
        (500, 900, 600),
        (1400, 1700, 800),
        (2500, 3000, 1000),
    ]
}

results = []

for file_name, ranges in extractions.items():
    file_path = os.path.join(folder, file_name)
    if not os.path.exists(file_path):
        print(f"File not found: {file_name}")
        continue

    df = pd.read_csv(file_path)
    if not all(col in df.columns for col in ["time", "eA", "eB", "eC"]):
        print(f"Missing expected columns in {file_name}")
        continue

    for (start, end, load) in ranges:
        subset = df[(df["time"] >= start) & (df["time"] <= end)]
        if subset.empty:
            print(f"No data found in {file_name} for {start}-{end}")
            continue

        avg_eA = subset["eA"].mean()
        avg_eB = subset["eB"].mean()
        avg_eC = subset["eC"].mean()

        results.append({
            "File": file_name,
            "Load_g": load,
            "Time_Start": start,
            "Time_End": end,
            "Avg_eA": avg_eA,
            "Avg_eB": avg_eB,
            "Avg_eC": avg_eC
        })

output_df = pd.DataFrame(results)
output_file = "cantilever_load_tests.csv"
output_df.to_csv(output_file, index=False)
print(f"Averages successfully saved to {output_file}")
