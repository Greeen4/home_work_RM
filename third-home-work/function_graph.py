import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative


def f(x):
    return np.sin(x)


def derivat(x):
    return derivative(f, x, dx=1e-6)


if __name__ == '__main__':
    x = np.arange(0,4*np.pi,0.1)
    
    plt.plot(x, f(x), label='f(x) = sinx')
    plt.plot(x, derivat(x), label='f\'(x)')
    
    plt.legend()
    plt.show()
    
