from scipy.signal import find_peaks
import numpy as np

def detect_peaks(signal, prominence, distance):
    # Return peak indices + peak properties
    return find_peaks(signal, prominence=prominence, distance=distance)

def calculate_depths(signal, peaks, properties):
    # Compute depth = baseline - peak value using left_bases
    depths = []
    left_bases = properties["left_bases"]

    for p, lb in zip(peaks, left_bases):
        baseline = signal[lb]
        peak_val = signal[p]

        depths.append({
            "peak_index": p,
            "baseline_index": lb,
            "baseline_value": baseline,
            "peak_value": peak_val,
            "depth": baseline - peak_val
        })

    return depths

def calculate_fwhm(signal, wavelengths, peaks, left_bases):
    fwhms = []
    for p, lb in zip(peaks, left_bases):
        half = (signal[lb] + signal[p]) / 2
        left_idx = np.where(signal[:p] <= half)[0][-1] if np.any(signal[:p] <= half) else 0
        right_idx = p + np.where(signal[p:] >= half)[0][0] if np.any(signal[p:] >= half) else p
        fwhms.append({
            "peak_index": p,
            "wl_left": wavelengths[left_idx],
            "wl_right": wavelengths[right_idx],
            "fwhm": wavelengths[right_idx] - wavelengths[left_idx]
        })
    return fwhms


