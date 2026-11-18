
import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [1, 2], [2, 1], [2, 3],
    [8, 8], [9, 8], [8, 9]
])

k = 2

centroids = X[[0,5]].copy()

for iteration in range(100):
    old_centroids = centroids.copy()

    dist = np.linalg.norm(X[:, None] - centroids, axis=2)
    labels = np.argmin(dist, axis=1)

    for j in range(k):
        centroids[j] = X[labels == j].mean(axis=0)

    if np.allclose(old_centroids, centroids):
        break

for j in range(k):
    print("Cluster", j + 1, ":", X[labels == j])
print("Centroids:", centroids)
print("Converged at iteration:", iteration + 1)


plt.figure(figsize=(8, 6))

for j in range(k):
    plt.scatter(X[labels == j, 0], X[labels == j, 1],
                label=f'Cluster {j+1}', s=60)
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='X', s=100, color='red',
            label='Centroids')

plt.title("K-Means Clustering")
plt.xlabel("X")
plt.ylabel("Y")

plt.xlim(0, 10)
plt.ylim(0, 10)

plt.legend(loc='upper left', bbox_to_anchor=(1.02, 1))

plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

