import pandas as pd
import matplotlib.pyplot as plt
import glob
import os   
from scipy.signal import find_peaks
import seaborn as sns


folder = r"C:\Users\Marijus\OneDrive - Vilnius University\3 semestras\cern\cern_data_analysis_project\20250722_05nJ_06-10um_Spectras"
output_folder = r"C:\Users\Marijus\OneDrive - Vilnius University\3 semestras\cern\cern_data_analysis_project\results"
file = glob.glob(os.path.join(folder, "20250722_05nJ_08um.xlsx")) [0]
df = pd.read_excel(file, sheet_name="Calibration 1-Measurements")

wavelength_col = df.columns[0]
s_cols = [c for c in df.columns if c.endswith(" S ")]
# Invert the signal data
df[s_cols] = df[s_cols].max()-df[s_cols]
signal = df[s_cols[0]]

# Peak detection parameters
threshold = 0.05 
min_distance = 10

peaks, properties = find_peaks(signal.values, prominence=threshold, distance=min_distance)

# Plot original signal
plt.figure(figsize=(10,5))
plt.plot(df[wavelength_col], signal, label='Inverted signal')

# Overlay peaks as red dots
plt.scatter(df[wavelength_col].iloc[peaks],
            signal.values[peaks],
            color='red', s=50, label='Detected peaks')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Reflection (inverted)')
plt.legend()
plt.show()