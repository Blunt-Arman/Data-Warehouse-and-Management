import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram
import numpy as np
def plot_dendrogram(model, **kwargs):
 counts = np.zeros(model.children_.shape[0])
 n_samples = len(model.labels_)
 for i, merge in enumerate(model.children_):
     counts[i] = sum((1 if c < n_samples else counts[c-n_samples]) for c in merge)
 linkage_matrix = np.column_stack([model.children_, model.distances_, counts]).astype(float)
 dendrogram(linkage_matrix, **kwargs)
iris = load_iris()
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None).fit(iris.data)
plt.title('Hierarchical Clustering Dendrogram')
plot_dendrogram(model, truncate_mode='level', p=3)
plt.show()
