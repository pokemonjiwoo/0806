import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(1000)
plt.clf()
plt.hist(data, bins = 20, color = 'skyblue', edgecolor = 'black')

plt. title('histogram chart')

plt.xlabel('values')
plt.ylabel('frequency')
plt.show()
