from data_tools import load_signal
from plot_tools import plot_with_sliders

# Configuration
folder = r"C:\Users\Marijus\OneDrive - Vilnius University\3 semestras\cern\cern_data_analysis_project\20250722_05nJ_06-10um_Spectras"
filename = "20250722_05nJ_08um.xlsx"
column_suffix = " P "          
initial_prominence = 4          
initial_distance = 10


# Load signal
wavelengths, signal = load_signal(folder, filename, column_suffix)

# Plot with sliders and peak detection
plot_with_sliders(wavelengths, signal, initial_prominence, initial_distance)

