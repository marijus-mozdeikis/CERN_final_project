import pandas as pd
import os
import numpy as np

def load_signal(folder, filename, column_suffix):
    """Load wavelength array and inverted signal from an Excel file."""

    # --- Locate file ---
    file_path = os.path.join(folder, filename)
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # --- Load Excel sheet ---
    df = pd.read_excel(file_path, sheet_name="Calibration 1-Measurements")

    # --- Find the first column that ends with the given suffix ---
    p_cols = [col for col in df.columns if col.endswith(column_suffix)]
    if not p_cols:
        raise ValueError(f"No columns ending with '{column_suffix}' found")

    signal_col = p_cols[0]

    # --- Convert wavelength + signal column to numeric ---
    df[df.columns[0]] = pd.to_numeric(df[df.columns[0]], errors="coerce")
    df[signal_col] = pd.to_numeric(df[signal_col], errors="coerce")

    # --- Extract arrays ---
    wavelengths = df[df.columns[0]].values
    signal_raw = df[signal_col].values

    # --- Invert signal (dip detection) ---
    signal = np.nanmax(signal_raw) - signal_raw

    return wavelengths, signal

