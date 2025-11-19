import numpy as np 
import matplotlib.pyplot as plt

fig,ax = plt.subplots(1,1)
n = 1

while True:
    graph = np.random.normal(0,10,4*40)
    graph = np.reshape(graph,(4*40 // 2,2))
    fft = np.fft.fft2(graph)
    
    ax.clear()
    ax.plot(np.abs(fft),c='red',linewidth=0.5,marker='o')

    plt.pause(n / 10)

plt.show()
