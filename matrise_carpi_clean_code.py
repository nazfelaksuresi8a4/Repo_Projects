import numpy as np
import matplotlib.pyplot as plt

x = 60
shape = [x]*x
matrix = np.linspace(0,shape,x)

for index in range(len(matrix)-1):
	matrix[index][index] = 0
	matrix[index][x-index-1] = 0
	
plt.imshow(matrix)
plt.show()