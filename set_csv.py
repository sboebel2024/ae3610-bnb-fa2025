import os
import pandas as pd

folder = "A_8Y_export"

for filename in os.listdir(folder):
    if filename.endswith(".xlsx"):
        excel_path = os.path.join(folder, filename)
        csv_name = os.path.splitext(filename)[0] + ".csv"
        csv_path = os.path.join(folder, csv_name)

        df = pd.read_excel(excel_path, sheet_name=None)  # read all sheets

        if len(df) > 1:
            for sheet_name, data in df.items():
                sheet_csv_path = os.path.join(folder, f"{os.path.splitext(filename)[0]}_{sheet_name}.csv")
                data.to_csv(sheet_csv_path, index=False)
                print(f"Converted {filename} ({sheet_name}) → {sheet_csv_path}")
        else:
            
            first_sheet = next(iter(df.values()))
            first_sheet.to_csv(csv_path, index=False)
            print(f"Converted {filename} → {csv_path}")

print("🎉 All Excel files have been converted to CSVs.")
