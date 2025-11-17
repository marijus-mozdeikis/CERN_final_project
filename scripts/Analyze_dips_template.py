import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import glob
import os   
from scipy.signal import find_peaks
import seaborn as sns
import numpy as np


folder = r"C:\Users\Marijus\OneDrive - Vilnius University\3 semestras\cern\cern_data_analysis_project\20250722_05nJ_06-10um_Spectras"
output_folder = r"C:\Users\Marijus\OneDrive - Vilnius University\3 semestras\cern\cern_data_analysis_project\results"

file = glob.glob(os.path.join(folder, "20250722_05nJ_08um.xlsx")) [0]
df = pd.read_excel(file, sheet_name="Calibration 1-Measurements")

# Invert the signal
wavelengths = df[df.columns[0]].values
p_cols = [c for c in df.columns if c.endswith(" P ")]
df[p_cols] = df[p_cols].max()-df[p_cols]
signal_values = df[p_cols[0]].values

# Initial peak detection parameters
threshold = 4
min_distance = 10
peaks, properties = find_peaks(signal_values, prominence=threshold, distance=min_distance)

# Initialize plot
fig, ax = plt.subplots(figsize=(10,5))
plt.subplots_adjust(bottom=0.25)
line_signal, = ax.plot(wavelengths, signal_values, label='Signal')
scatter_peaks = ax.scatter(wavelengths[peaks], signal_values[peaks], color='red', s=50, label='Peaks')
ax.set_xlabel('Wavelength (nm)')
ax.set_ylabel('Reflection (inverted)')
ax.legend()

# Add sliders
ax_prom = plt.axes([0.25, 0.1, 0.65, 0.03])
ax_dist = plt.axes([0.25, 0.15, 0.65, 0.03])

slider_prom = Slider(ax_prom, 'Prominence', 0, 10, valinit=threshold, valstep=0.5)
slider_dist = Slider(ax_dist, 'Min Distance', 0, 50, valinit=min_distance, valstep=2)

# Update function
def update(val):
    prom = slider_prom.val
    dist = int(slider_dist.val)
    peaks, properties = find_peaks(signal_values, prominence=prom, distance=dist)
    
    scatter_peaks.set_offsets(np.c_[wavelengths[peaks], signal_values[peaks]])
    fig.canvas.draw_idle()

# Connect sliders
slider_prom.on_changed(update)
slider_dist.on_changed(update)

plt.show()