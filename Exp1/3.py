import numpy as np
import matplotlib.pyplot as plt

def unit_step(length, position):
    signal = np.zeros(length)
    signal[position:] = 1
    return signal

x = np.arange(-10, 10, 1)
step = unit_step(len(x), -(-10))
plt.stem(x, step)
plt.title("Unit Step Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
