import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
class_A = np.random.normal(loc=1.0, scale=0.3, size=(50, 2))
class_B = np.random.normal(loc=4.0, scale=0.3, size=(50, 2))
X = np.vstack((class_A, class_B))
y = np.array([0]*50 + [1]*50) 

# Function to evaluate intraclass and interclass distances
def evaluate_intraclass_interclass(X, y):
    class_labels = np.unique(y)
    class1, class2 = class_labels[:2]

    X1 = X[y == class1]
    X2 = X[y == class2]

    # Calculate centroids
    centroid1 = np.mean(X1, axis=0)
    centroid2 = np.mean(X2, axis=0)

    # Calculate spread (standard deviation)
    spread1 = np.std(X1, axis=0)
    spread2 = np.std(X2, axis=0)

    # Calculate interclass distance
    interclass_distance = np.linalg.norm(centroid1 - centroid2)

    return centroid1, centroid2, spread1, spread2, interclass_distance
centroid1, centroid2, spread1, spread2, inter_dist = evaluate_intraclass_interclass(X, y)
print("Centroid of Class A:", centroid1)
print("Centroid of Class B:", centroid2)
print("Spread (Std Dev) of Class A:", spread1)
print("Spread (Std Dev) of Class B:", spread2)
print("Interclass Distance between Centroids:", inter_dist)

# Optional: Plotting the visual like the diagram
plt.scatter(class_A[:, 0], class_A[:, 1], color='blue', label='Class A')
plt.scatter(class_B[:, 0], class_B[:, 1], color='red', label='Class B')
plt.scatter(*centroid1, color='black', marker='x', s=100, label='Centroid A')
plt.scatter(*centroid2, color='black', marker='x', s=100, label='Centroid B')
plt.plot([centroid1[0], centroid2[0]], [centroid1[1], centroid2[1]], color='cyan', linestyle='--', label='Interclass Distance')
plt.title("Intraclass Spread and Interclass Distance")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()
