import matplotlib.pyplot as plt


def plot(x, y):
    plt.plot(x, y)
    plt.show()


def plot_matrix(matrix):
    plt.plot(matrix)
    plt.show()


def example():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256]
    plot(x, y)


if __name__ == '__main__':
    example()
