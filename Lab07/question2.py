import numpy as np
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
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

# plt.scatter(Xpca[:, 0], Xpca[:, 1], c=y, cmap=plt.cm.Set1)
# plt.show()

K = 3
h_kmeans = KMeans(n_clusters=K)
h_kmeans.fit(X)
y_kmeans = h_kmeans.predict(X)
C = h_kmeans.cluster_centers_

fh = plt.figure(figsize=(8, 6))
fh.add_subplot(2, 1, 1)
plt.scatter(Xpca[:, 0], Xpca[:, 1], c=y, cmap=plt.cm.Set1)
plt.title("2D visualisation of iris data (true clusters)")

fh.add_subplot(2, 1, 2)
# plt.scatter(Xpca[:, 0], Xpca[:, 1], c=y_kmeans, cmap=plt.cm.Set1)
plt.scatter(C[:, 0], C[:, 1], c=range(K),
            cmap=plt.cm.Set1,
            marker='s', edgecolor='black')
plt.title("2D visualisation of iris data (true clusters)")

plt.show()