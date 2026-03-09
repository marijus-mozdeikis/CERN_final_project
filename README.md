# Resonance Analysis Tool

Python tool for analyzing plasmonic resonance reflection spectra. Processes xslx files containing spectra measurements to locate resonances and extract their properties with manual parameter adjustment.

## What It Does
- Loads reflection spectra from Excel files
- Inverts signals to detect resonance dips as peaks  
- Interactive plots with sliders for peak detection tuning
- Clickable baseline adjustment for accurate depth and FWHM measurement
- Calculates: resonance wavelength, depth, FWHM, Q factor, MQ factor
- Exports results to Excel with controlled positioning
- Handles one sample measurements (one xslx file) at once. Distinguish between P and S polarization, different incident angles spectra with correct resonance ordering

## Required Packages

- pandas, numpy, scipy, matplotlib, openpyxl
- python 3.14.0