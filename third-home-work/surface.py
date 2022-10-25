import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np


def surface():
    x = np.linspace(-15, 20, 50)
    y = np.linspace(-15, 20, 50)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
      
    ax = plt.axes(projection ='3d') 
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap='viridis')
    
    plt.title('f(x,y) = x^2 - y^2')
    plt.show()


def f(x, y):
    return x**2 - y**2 


def choose_mode():
    print('Input number of mode:\n1. surface\n2. direction field')

    mode = int(input('-> '))

    if mode != 1 and mode != 2:
        raise Exception('Choose the correct number')
    
    return mode


def direction_field():
    x = np.linspace(-5, 10, 20)
    y = np.linspace(-5, 10, 20)

    X, Y = np.meshgrid(x, y)

    dx = 2 * X
    dy = -2 * Y 

    norm_dx = dx / np.sqrt(X ** 2 + Y ** 2)
    norm_dy = dy / np.sqrt(X ** 2 + Y ** 2)

    plt.quiver(X, Y, norm_dx, norm_dy)
    plt.title('Direction field of f(x,y) = x^2 - y^2')

    plt.show()


def main():
    try:
        mode = choose_mode()

    except Exception as e:
        print(e)
        exit(0)

    if mode == 1: surface()
    else: direction_field() 


if __name__ == "__main__":
    main()
