import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Aprendizado não supervisionado

# Criando dados de exemplo (duas características)
data = np.array([[2, 3], [5, 8], [1, 2], [8, 8], [1, 1], [9, 10]])

# Criando o modelo K-Means com 2 clusters
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

# Obtendo as etiquetas de cluster para cada ponto
labels = kmeans.labels_

# Obtendo os centróides dos clusters
centroids = kmeans.cluster_centers_

# Plotando os dados e os centróides
plt.scatter(data[:, 0], data[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, c='red')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.title('Agrupamento com K-Means')
plt.show()
