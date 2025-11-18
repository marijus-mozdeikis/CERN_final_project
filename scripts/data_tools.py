# data_tools.py
import pandas as pd
import os
import glob
import numpy as np

def load_signal(folder, filename, COLUMN_SUFFIX=" P "):
    """
    Load wavelengths and inverted signal from Excel file.
    
    Parameters:
        folder (str): folder containing Excel file
        filename (str): name of the Excel file
        COLUMN_SUFFIX (str): suffix for signal columns
    
    Returns:
        wavelengths (np.ndarray): array of wavelengths
        signal (np.ndarray): inverted signal values
    """
    # Locate file
    file_path = os.path.join(folder, filename)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Load Excel sheet
    df = pd.read_excel(file_path, sheet_name="Calibration 1-Measurements")
    
    # Find signal columns
    p_cols = [c for c in df.columns if c.endswith(COLUMN_SUFFIX)]
    if len(p_cols) == 0:
        raise ValueError(f"No columns ending with '{COLUMN_SUFFIX}' found")
    
    # Convert to numeric (in case Excel has strings)
    df[p_cols] = df[p_cols].apply(pd.to_numeric, errors='coerce')
    
    # Select first signal column
    signal_col = p_cols[0]
    
    # Extract wavelengths (first column assumed)
    wavelengths = pd.to_numeric(df[df.columns[0]], errors='coerce').values
    
    # Invert signal
    signal = df[signal_col].max() - df[signal_col].values
    
    # Remove any NaNs (optional)
    mask = ~np.isnan(wavelengths) & ~np.isnan(signal)
    wavelengths = wavelengths[mask]
    signal = signal[mask]
    
    print("First 5 wavelengths:", wavelengths[:5])
    print("First 5 signal values:", signal[:5])
    
    return wavelengths, signal
