import numpy as np
import matplotlib.pyplot as plt


def symmetric_limits(data):
    lim = max(-data.min(), data.max())
    return {'vmin': -lim, 'vmax': lim}


def case1_single_line_plot():
    x = [1, 2, 3, 4, 5]
    y = [3, 2, 4, 1, 1]
    plt.plot(x, y)
    plt.show()


def case2_multi_line_plot():
    x = [1, 2, 3, 4, 5]
    y1 = [3, 2, 4, 1, 1]
    y2 = [4, 1, 3, 2, 0]
    y3 = [4.2, 0.8, 2, 2, 1]
    lines = plt.plot(x, y1, x, y2, x, y3)
    plt.legend(lines, ['y1', 'y2', 'y3'])
    plt.show()


def case3_filled_contours():
    x, y = np.mgrid[-3:3:50j, -3:3:50j]
    g = np.exp(-0.5*(x**2 + y**2)) - 1.3*np.exp(-0.5*(x**2 + 2*y**2))
    plt.contourf(x, y, g, **symmetric_limits(g))
    plt.show()


def case4_pseudocolor():
    x, y = np.mgrid[-3:3:50j, -3:3:50j]
    g = np.exp(-0.5*(x**2 + y**2)) - 1.3*np.exp(-0.5*(x**2 + 2*y**2))
    plt.pcolor(x, y, g, **symmetric_limits(g))
    plt.show()


def case5_single_boxplot():
    x = [1, 5, 5.1, 5.1, 5.5, 5.4, 5.5, 5.4, 5.6, 5.7, 6., 6.1, 9]
    plt.boxplot(x)
    plt.show()


if __name__ == '__main__':
    plt.style.use('ifr')
    # plt.style.use(['ifr', 'grayscale'])
    # case1_single_line_plot()
    # case2_multi_line_plot()
    # case3_filled_contours()
    # case4_pseudocolor()
    case5_single_boxplot()
