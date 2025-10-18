import pandas as pd

# print the table we need for #7 in DR requirements

Xg_in = 0.9
L1_in = 10.0
L2_in = 11 + 3/16
t_in = 0.1260
b_in = 1.025

Xg = Xg_in * 0.0254
L1 = L1_in * 0.0254
L2 = L2_in * 0.0254
t = t_in * 0.0254
b = b_in * 0.0254

I = b * t**3 / 12
mP_micro = 85.88
mD_micro = 6.56e4
mP = mP_micro * 1e-6
mD = mD_micro * 1e-6

E = ((L2 - Xg) * t) / (2 * I * mP)
EI = E * I

data = {
    "Quantity": [
        "Strain–Load slope (µε/N)",
        "Strain–Deflection slope (µε/m)",
        "Gauge position Xg (m)",
        "Prescribed disp. point L1 (m)",
        "Load point L2 (m)",
        "Thickness t (m)",
        "Width b (m)",
        "Moment of inertia I (m^4)",
        "Elastic modulus E (Pa)",
        "Effective stiffness EI (N·m^2)"
    ],
    "Value": [
        mP_micro,
        mD_micro,
        Xg,
        L1,
        L2,
        t,
        b,
        I,
        E,
        EI
    ]
}

df = pd.DataFrame(data)
df.to_csv("beam_properties.csv", index=False)
print(df)
