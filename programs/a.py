import matplotlib.pyplot as plt
from numpy.random import normal
gaussian_numbers = normal(size=1000)
a = [1,2,3,4,5,2,6,4,1,5,0]
print gaussian_numbers
plt.hist(a)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
