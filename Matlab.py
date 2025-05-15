import matplotlib.pyplot as plt
import numpy as np

x = "Ronaldo"

figure,ax = plt.figure(figsize=(5,4))

fig,ax = figure.subplots()

ax.ecdf(np.linspace(0,10,100))

plt.show()

