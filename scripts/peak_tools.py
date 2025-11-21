from scipy.signal import find_peaks

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
