import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**(3/4) - 2*x**2 + 6*x - 1/5

x = np.linspace(1, 6, 100)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de f(x)')
plt.grid(True)
plt.show()