# run.py
from data_tools import load_signal
from plot_tools import plot_with_sliders

# ----------------- CONFIGURATION -----------------
FOLDER = r"C:\Users\Marijus\OneDrive - Vilnius University\3 semestras\cern\cern_data_analysis_project\20250722_05nJ_06-10um_Spectras"
FILENAME = "20250722_05nJ_08um.xlsx"
COLUMN_SUFFIX = " P "          # column ending for signal
INITIAL_PROMINENCE = 4
INITIAL_DISTANCE = 10
# -------------------------------------------------

# Load signal
wavelengths, signal = load_signal(FOLDER, FILENAME, COLUMN_SUFFIX=COLUMN_SUFFIX)

# Plot with sliders and peak detection
plot_with_sliders(wavelengths, signal, init_prom=INITIAL_PROMINENCE, init_dist=INITIAL_DISTANCE)

