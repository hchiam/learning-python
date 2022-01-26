# https://towardsdatascience.com/independent-component-analysis-ica-in-python-a0ef0db0955e

# https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html

# python ica.py

from sklearn.datasets import load_digits
from sklearn.decomposition import FastICA
import matplotlib.pyplot as plt
from plot_graph import plot_matrix


def example():
    X, _ = load_digits(return_X_y=True)
    transformer = FastICA(n_components=7,
                          random_state=0,
                          tol=0.1)
    X_transformed = transformer.fit_transform(X)
    print(X_transformed.shape)
    # (1797, 7)

    plot_matrix(X_transformed)


if __name__ == '__main__':
    example()
