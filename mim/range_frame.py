import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import matplotlib as mpl


def range_frame(x, y, ax, fmt='%.2f'):
    q = (0, 25, 50, 75, 100)
    for observations, loc, axis in zip([x, y],
                                       ['bottom', 'left'],
                                       [ax.xaxis, ax.yaxis]):
        stats = np.percentile(observations, q)
        ax.spines[loc].set_bounds(stats[1], stats[3])
        axis.set_ticks(stats)
        axis.set_major_formatter(FormatStrFormatter(fmt))


if __name__ == '__main__':
    x, y = np.random.randn(2, 100)

    mpl.style.use('ifr')
    plt.scatter(x, y)
    range_frame(x, y, plt.gca())
    plt.show()
