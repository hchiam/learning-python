# https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60

# https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html

# python pca.py

import numpy as np
from sklearn.decomposition import PCA


def example():
    data_points = np.array(
        [[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    pca = PCA(n_components=2)
    pca.fit(data_points)

    print(pca.explained_variance_ratio_)
    # [0.99244289 0.00755711]

    print(pca.singular_values_)
    # [6.30061232 0.54980396]


if __name__ == '__main__':
    example()
