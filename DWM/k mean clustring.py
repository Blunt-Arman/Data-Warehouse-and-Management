l = list(map(int, input("Numbers (comma-separated): ").split(",")))
k = int(input("Enter K: "))
centroids = l[:k]
while True:
 clusters = [[] for _ in range(k)]
 for val in l:
     idx = min(range(k), key=lambda i: abs(val - centroids[i]))
     clusters[idx].append(val)
     new_centroids = [sum(c)/len(c) if c else centroids[i] for i, c in enumerate(clusters)]
 if new_centroids == centroids:
     break
 centroids = new_centroids
print("Final Clusters:", clusters)
print("Centroids:", centroids)
