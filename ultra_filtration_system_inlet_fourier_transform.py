import datetime
import numpy as np
import scipy as sp
import scipy.fftpack
import pandas as pd
import matplotlib.pyplot as plt

###############################
# example from ipython cook book 
###############################


#https://ipython-books.github.io/101-analyzing-the-frequency-components-of-a-signal-with-a-fast-fourier-transform/


pressure_inlet_ultra_filtration_30days = pd.read_pickle("pressure_inlet_ultra_filtration_30days.pickle")

pressure_inlet_ultra_filtration_30days.plot(figsize=(20, 15))

pressure_inlet_ultra_filtration_30days.info()




# 6.  We now compute the Fourier transform and the spectral density of the signal. 
# The first step is to compute the FFT of the signal using the fft() function:


temp_fft = sp.fftpack.fft(pressure_inlet_ultra_filtration_30days["Pressure_bar"].values)

# 7.  Once the FFT has been obtained, we need to take the square of its absolute value in order to get the power spectral density (PSD):

temp_psd = np.abs(temp_fft) ** 2

# 8.  The next step is to get the frequencies corresponding to the values of the PSD. The fftfreq() utility function does just that. 
# It takes the length of the PSD vector as input as well as the frequency unit.
# Here, we choose an annual unit: a frequency of 1 corresponds to 1 year (365 days). We provide 1/365 because the original unit is in days:

fftfreq = sp.fftpack.fftfreq(len(temp_psd), 1. / 30)

# 9.  The fftfreq() function returns positive and negative frequencies. 
# We are only interested in positive frequencies here, as we have a real signal:

i = fftfreq > 0


#10.  We now plot the power spectral density of our signal, as a function of the frequency (in unit of 1/year).
# We choose a logarithmic scale for the y axis (decibels):


fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.plot(fftfreq[i], 10 * np.log10(temp_psd[i]))
ax.set_xlim(0, 5)
ax.set_xlabel('Frequency (1/30 days)')
ax.set_ylabel('PSD (dB)')


#####################################################################################
##Another example 

#Generating the fourier transform of the two data series

pressure_inlet_ultra_filtration_30days_fft = rfft(pressure_inlet_ultra_filtration_30days["Pressure_bar"].values)


#Taking the absolute value of the fft and scaling the amplitude
pressure_inlet_ultra_filtration_30days_fft = (1/((len(pressure_inlet_ultra_filtration_30days_fft) - 1) * 2)) * np.abs(pressure_inlet_ultra_filtration_30days_fft)

#Creating Frequency Values in Hz
pressure_inlet_ultra_filtration_30days_frenquency = 1 / ((1 / ((np.arange(0, len(pressure_inlet_ultra_filtration_30days_fft))) * 100)) * 60 * 60 * 24)     #Period X Axis


#draw the chart 


#%matplotlib qt
import matplotlib.pyplot as plt

# Creating a Figure and Axes to plot on
fig, ax = plt.subplots(1)

# Plotting the inlet pressure
ax.plot(pressure_inlet_ultra_filtration_30days_frenquency, pressure_inlet_ultra_filtration_30days_fft, label = "ultra filtration inlet")

# Adding Labels to the Graph Axes
ax.set_xlabel("Period (Days)", fontsize = 24)
ax.set_ylabel("pressure in bars", fontsize = 24)
ax.set_title("Tinsley Bridge ultra filtration system", fontsize = 24)

ax.legend(loc='lower left', bbox_to_anchor=(0.5, -0.05),shadow=True, ncol=6)

#Setting limits and scales
ax.set_xlim([-0.1, 5])
ax.set_ylim([0, 3])

# Adding a Grid to the Graph for Readability
ax.grid()

