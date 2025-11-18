# peak_tools.py
from scipy.signal import find_peaks

def detect_peaks(signal, prominence, distance):
    """Detect peaks and return indices and properties."""
    peaks, properties = find_peaks(signal, prominence=prominence, distance=distance)
    return peaks, properties

def calculate_depths(signal, peaks, properties):
    """Calculate depth for each peak using left baseline."""
    depths = []
    left_bases = properties["left_bases"]
    for p, lb in zip(peaks, left_bases):
        baseline_value = signal[lb]
        peak_value = signal[p]
        depth = baseline_value - peak_value
        depths.append({
            "peak_index": p,
            "baseline_index": lb,
            "baseline_value": baseline_value,
            "peak_value": peak_value,
            "depth": depth
        })
    return depths
