# plot_tools.py
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
from peak_tools import detect_peaks, calculate_depths

def plot_with_sliders(wavelengths, signal, init_prom=4, init_dist=10):
    """Plot signal with peaks and left baseline, interactive sliders for prominence and distance."""
    peaks, props = detect_peaks(signal, init_prom, init_dist)

    fig, ax = plt.subplots(figsize=(10,5))
    plt.subplots_adjust(bottom=0.25)

    ax.plot(wavelengths, signal, label="Signal")
    sc_peaks = ax.scatter(wavelengths[peaks], signal[peaks], s=50, color="red", label="Peaks")
    sc_base = ax.scatter(wavelengths[props["left_bases"]],
                         signal[props["left_bases"]], s=40, color="green", label="Left Baseline")

    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Reflection (inverted)")
    ax.legend()

    # Sliders
    ax_prom = plt.axes([0.25, 0.1, 0.65, 0.03])
    ax_dist = plt.axes([0.25, 0.15, 0.65, 0.03])
    slider_prom = Slider(ax_prom, "Prominence", 0, 10, valinit=init_prom, valstep=0.5)
    slider_dist = Slider(ax_dist, "Min Distance", 0, 50, valinit=init_dist, valstep=2)

    def update(_):
        prom = slider_prom.val
        dist = int(slider_dist.val)
        peaks, props = detect_peaks(signal, prom, dist)

        sc_peaks.set_offsets(np.c_[wavelengths[peaks], signal[peaks]])
        sc_base.set_offsets(np.c_[wavelengths[props["left_bases"]],
                                  signal[props["left_bases"]]])

        depths = calculate_depths(signal, peaks, props)
        print("\nDetected dips:")
        for d in depths:
            print(f"λ={wavelengths[d['peak_index']]:.2f} | "
                  f"Left baseline λ={wavelengths[d['baseline_index']]:.2f} | "
                  f"Baseline={d['baseline_value']:.2f} | "
                  f"Depth={d['depth']:.2f}")

        fig.canvas.draw_idle()

    slider_prom.on_changed(update)
    slider_dist.on_changed(update)

    update(None)  # initial display
    plt.show()
