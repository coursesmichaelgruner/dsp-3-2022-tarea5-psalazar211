import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
import scipy.signal as signal
import math
from plot_zplane import zplane 

Fs, noisy_signal = waves.read("la_muerte_del_angel_power_noise.wav")
print(Fs)

Time = np.linspace(0, len(noisy_signal) / Fs, num=len(noisy_signal))

plt.figure(1)
plt.title("Signal Wave")
plt.plot(Time, noisy_signal)
#plt.show()

# DTF
N = len(noisy_signal)
yf = fft(noisy_signal)
freq = fftfreq(N)
freq_in_Hz = abs(freq * Fs)
plt.figure(2)
plt.title("Frecuency Domain")
plt.xlabel("Hz")
plt.plot(freq_in_Hz,np.abs(yf))
#plt.show()

# Ventana 0
N = len(noisy_signal)
yf = fft(noisy_signal)
freq = fftfreq(N)
freq_in_Hz = abs(freq * Fs)
yf = yf[0:10000]
freq_in_Hz = freq_in_Hz[0:10000]
plt.figure(3)
plt.title("Frecuency Domain")
plt.xlabel("Hz")
plt.plot(freq_in_Hz,np.abs(yf))
#plt.show()


# Ventana 1
N = len(noisy_signal)
yf = fft(noisy_signal)
freq = fftfreq(N)
freq_in_Hz = abs(freq * Fs)
yf = yf[0:2500]
freq_in_Hz = freq_in_Hz[0:2500]
plt.figure(4)
plt.title("Frecuency Domain")
plt.xlabel("Hz")
plt.plot(freq_in_Hz,np.abs(yf))
#plt.show()

# Ventana 2
N = len(noisy_signal)
yf = fft(noisy_signal)
freq = fftfreq(N)
freq_in_Hz = abs(freq * Fs)
yf = yf[2500:5000]
freq_in_Hz = freq_in_Hz[2500:5000]
plt.figure(5)
plt.title("Frecuency Domain")
plt.xlabel("Hz")
plt.plot(freq_in_Hz,np.abs(yf))
#plt.show()

# Ventana 3
N = len(noisy_signal)
yf = fft(noisy_signal)
freq = fftfreq(N)
freq_in_Hz = abs(freq * Fs)
yf = yf[5000:7500]
freq_in_Hz = freq_in_Hz[5000:7500]
plt.figure(6)
plt.title("Frecuency Domain")
plt.xlabel("Hz")
plt.plot(freq_in_Hz,np.abs(yf))
#plt.show()

# Ventana 4
N = len(noisy_signal)
yf = fft(noisy_signal)
freq = fftfreq(N)
freq_in_Hz = abs(freq * Fs)
yf = yf[7500:10000]
freq_in_Hz = freq_in_Hz[7500:10000]
plt.figure(7)
plt.title("Frecuency Domain")
plt.xlabel("Hz")
plt.plot(freq_in_Hz,np.abs(yf))
#plt.show()


#b = np.array([0, 1, 1])
#a = np.array([1, 1/4., -3/8.])
#zplane(b,a)

Fs1, ref_signal = waves.read("la_muerte_del_angel.wav")
print(Fs)

Time1 = np.linspace(0, len(ref_signal) / Fs1, num=len(ref_signal))

plt.figure(21)
plt.title("Signal Wave")
plt.plot(Time1, ref_signal)
#plt.show()



b1 = [1,-2*math.cos(math.pi*0.0025*1),1] 
a1 = [1,-2*0.95*math.cos(math.pi*0.0025*1),0.95**2]
w, h = signal.freqz(b1,a1)
fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')
ax1.plot(w, (abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
ax2.plot(w, angles, 'g')
ax2.set_ylabel('Angle (radians)', color='g')
ax2.grid(True)
ax2.axis('tight')
#plt.show()

b2 = [1,-2*math.cos(math.pi*0.0025*2),1] 
a2 = [1,-2*0.95*math.cos(math.pi*0.0025*2),0.95**2]
w, h = signal.freqz(b2,a2)
fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')
ax1.plot(w, (abs(h)), 'b')
ax1.set_ylabel('Amplitude', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
#plt.show()
b3 = [1,-2*math.cos(math.pi*0.0025*3),1] 
a3 = [1,-2*0.95*math.cos(math.pi*0.0025*3),0.95**2]
w, h = signal.freqz(b1,a1)
fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')
ax1.plot(w, (abs(h)), 'b')
ax1.set_ylabel('Amplitude', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
#plt.show()
b4 = [1,-2*math.cos(math.pi*0.0025*4),1] 
a4 = [1,-2*0.95*math.cos(math.pi*0.0025*4),0.95**2]
w, h = signal.freqz(b1,a1)
fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')
ax1.plot(w, (abs(h)), 'b')
ax1.set_ylabel('Amplitude', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
#plt.show()
b5 = [1,-2*math.cos(math.pi*0.0025*5),1] 
a5 = [1,-2*0.95*math.cos(math.pi*0.0025*5),0.95**2]
w, h = signal.freqz(b1,a1)
fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')
ax1.plot(w, (abs(h)), 'b')
ax1.set_ylabel('Amplitude', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
#plt.show()
b6 = [1,-2*math.cos(math.pi*0.0025*6),1] 
a6 = [1,-2*0.95*math.cos(math.pi*0.0025*6),0.95**2]
w, h = signal.freqz(b1,a1)
fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')
ax1.plot(w, (abs(h)), 'b')
ax1.set_ylabel('Amplitude', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
#plt.show()
b7 = [1,-2*math.cos(math.pi*0.0025*7),1] 
a7 = [1,-2*0.95*math.cos(math.pi*0.0025*7),0.95**2]
w, h = signal.freqz(b1,a1)
fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')
ax1.plot(w, (abs(h)), 'b')
ax1.set_ylabel('Amplitude', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
#plt.show()


output1 = signal.filtfilt(b1, a1, noisy_signal)
output2 = signal.filtfilt(b2, a2, output1)
output3 = signal.filtfilt(b3, a3, output2)
output4 = signal.filtfilt(b4, a4, output3)
output5 = signal.filtfilt(b5, a5, output4)
output6 = signal.filtfilt(b6, a6, output5)
output7 = signal.filtfilt(b7, a7, output6)
plt.plot(Time, output7, label='filtered')
plt.legend()
plt.show()
 
zplane(a1,b1)
zplane(a2,b2)
zplane(a3,b3)
zplane(a4,b4)
zplane(a5,b5)
zplane(a6,b6)
zplane(a7,b7)
