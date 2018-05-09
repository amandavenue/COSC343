import numpy as np
from datasets import datasets
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

mnist = datasets.load_mnist()
X = mnist.data
y = mnist.target

muX = np.mean(X, axis=0)
X -= muX

h_pca = PCA()
h_pca.fit(X)

Xpca = h_pca.transform(X)

K = 10
h_kmeans = KMeans(n_clusters=K, n_init=1)
h_kmeans.fit(X)
y_kmeans = h_kmeans.predict(X)
C = h_kmeans.cluster_centers_

fh = plt.figure(figsize=(8, 6))
fh.add_subplot(2, 1, 1)
plt.scatter(Xpca[:500, 0], Xpca[:500, 1], c=y[:500], cmap=plt.cm.Set1)
plt.title("2D visualisation of iris data (true clusters)")

fh.add_subplot(2, 1, 2)
plt.scatter(Xpca[:500, 0], Xpca[:500, 1], c=y_kmeans[:500], cmap=plt.cm.Set1)
Cpca = h_pca.transform(C)
plt.scatter(Cpca[:, 0], Cpca[:, 1], c=range(K),
            cmap=plt.cm.Set1,
            marker='s', edgecolor='black')
plt.title("2D visualisation of iris data (true clusters)")

mnist.show(C)

plt.show()