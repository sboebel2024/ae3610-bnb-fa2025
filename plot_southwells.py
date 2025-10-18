import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def southwell_strain_plot(filename, title, output_plot, L_in, h_in):
    df = pd.read_csv(filename)

    # Correct bending strain definition, no scaling factor
    df["eps_bend"] = abs((df["SG_Adapter_A_pct"] - df["SG_Adapter_B_pct"]) / 2) / 100
    df["eps_over_P"] = df["eps_bend"] / abs(df["Force_N"])

    x = df["eps_over_P"]
    y = df["eps_bend"]
    m, b = np.polyfit(x, y, 1)
    y_fit = m * x + b
    r2 = 1 - np.sum((y - y_fit)**2) / np.sum((y - np.mean(y))**2)

    L_m = L_in * 0.0254
    h_m = h_in * 0.0254
    Pcr = m  # direct slope-based Pcr (the ~927 N one)

    plt.figure(figsize=(7,5))
    plt.plot(x, y, 'ko', markersize=5, label="Data")
    plt.plot(
        x,
        y_fit,
        color='black',
        linestyle=(0, (1, 2)),  # dashed fit line
        linewidth=1.2,
        label=f"Fit: y={m:.3e}x+{b:.3e}\nR²={r2:.4f}\nPcr={Pcr:.2f} N"
    )
    plt.xlabel("ε_bend / P  (1/N)", color="black", fontsize=12)
    plt.ylabel("ε_bend", color="black", fontsize=12)
    plt.grid(True, linestyle='--', color='0.5', alpha=0.8)
    plt.legend(edgecolor="black", facecolor="white", fontsize=9)
    plt.tight_layout()
    plt.savefig(output_plot, dpi=600, bbox_inches="tight", facecolor="white")
    plt.show()

    print(f"{title}:\n  slope (Pcr) = {m:.3e} N\n  intercept = {b:.3e}\n  R² = {r2:.4f}")

southwell_strain_plot("long_column_tests.csv", "Southwell Plot – Long Column (B&W)", "southwell_long_bw.png", L_in=29, h_in=0.50)
southwell_strain_plot("short_column_tests.csv", "Southwell Plot – Short Column (B&W)", "southwell_short_bw.png", L_in=24, h_in=0.50)
