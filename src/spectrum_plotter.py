import numpy as np
import matplotlib.pyplot as plt

def plot_signal(filename="capture.bin", sample_rate=2e6):
    data = np.fromfile(filename, dtype=np.uint8)
    data = data.astype(np.float32) - 127.5
    iq = data[::2] + 1j * data[1::2]
    spectrum = np.fft.fftshift(np.fft.fft(iq))
    plt.plot(20*np.log10(np.abs(spectrum)))
    plt.title("SDR Spectrum")
    plt.xlabel("Frequency Bin")
    plt.ylabel("Magnitude (dB)")
    plt.show()

if __name__ == "__main__":
    plot_signal()
