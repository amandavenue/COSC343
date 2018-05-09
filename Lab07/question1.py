import numpy as np
from sklearn import datasets
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris.data
y = iris.target

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 3], X[:, 1], c=y, cmap=plt.cm.Set1)
plt.show()

muX = np.mean(X, axis=0)
X -= muX

h_pca = PCA()
h_pca.fit(X)

print("Eigenvectors: ")
print(h_pca.components_)
print("Eigenvalues: ")
print(h_pca.explained_variance_ratio_)

Xpca = h_pca.transform(X)

plt.scatter(Xpca[:, 0], Xpca[:, 1], c=y, cmap=plt.cm.Set1)
plt.show()

