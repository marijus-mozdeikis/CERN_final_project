import pandas as pd
import glob
import os
import matplotlib.pyplot as plt
import re

# Folder path
folder = r"C:\Users\Marijus\OneDrive - Vilnius University\3 semestras\cern\cern_data_analysis_project\20250722_05nJ_06-10um_Spectras"
file = glob.glob(os.path.join(folder, "*.xlsx"))[0]

df = pd.read_excel(file, sheet_name="Calibration 1-Measurements")
wavelength_col = df.columns[0]
s_cols = [c for c in df.columns if c.endswith(" S ")]

def get_angle(col):
    angle = re.search(r'R (\d+)', col)
    return angle.group(1) + "°"

print(f"Working with: {os.path.basename(file)}")

plt.figure(figsize=(10, 5))
for col in s_cols:
    angle_label = get_angle(col)
    plt.plot(df[wavelength_col], df[col], label = angle_label)
plt.legend()
plt.title("S polarization: 0.8um, 0.5 nJ, Ag 50 nm ITO")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Reflection (%)")
plt.show()