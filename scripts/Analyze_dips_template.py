import pandas as pd
import matplotlib.pyplot as plt
import glob
import os   
from peakutils import baseline


folder = r"C:\Users\Marijus\OneDrive - Vilnius University\3 semestras\cern\cern_data_analysis_project\20250722_05nJ_06-10um_Spectras"
output_folder = r"C:\Users\Marijus\OneDrive - Vilnius University\3 semestras\cern\cern_data_analysis_project\results"
file = glob.glob(os.path.join(folder, "20250722_05nJ_08um.xlsx")) [0]
df = pd.read_excel(file, sheet_name="Calibration 1-Measurements")

wavelength_col = df.columns[0]
s_cols = [c for c in df.columns if c.endswith(" S ")]
df[s_cols] = -df[s_cols]


plt.plot(df[wavelength_col], df[s_cols[0]], label = s_cols[0])
plt.show()