import numpy as np
import matplotlib.pyplot as plt
from time import sleep

plt.style.use('dark_background')

amplitudes = [0.0,0.0,0.0,0.0,0.0,0.0,
              0.0,0.0,0.0,0.0,0.0,0.0,
              0.0,0.0,0.0,0.0,0.0,0.0,
              0.6,-0.1,0.0,0.0,0.0,0.0,
              0.0,0.0,0.0,0.0,0.0,0.0,
              0.0,0.0]

electrodiagram_array = []

length = len(amplitudes)
index = 0

x_lim_1 = 0
x_lim_2 = 34

fig,ax = plt.subplots(nrows=1,ncols=1)

for i in range(length*4):
    for j in range(length):
        amplitudes.append(amplitudes[j])

while True:
    if index >= length*1:
        index = 0
        electrodiagram_array.clear()

    
    electrodiagram_array.append(amplitudes[index])

    ax.clear()
    ax.plot(electrodiagram_array,c='g')
    print(electrodiagram_array)

    ax.set_xlim(x_lim_1,x_lim_2)

    index += 1

    plt.pause(0.050)
