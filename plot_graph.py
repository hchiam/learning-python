import matplotlib.pyplot as plt


def example():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256]

    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    example()
