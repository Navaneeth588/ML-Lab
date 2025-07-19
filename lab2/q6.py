# Input feature vectors
vector_X = [20, 6, 2, 386]
vector_Y = [16, 3, 6, 289]

# Calculate dot product using zip
dot_product = sum(a * b for a, b in zip(vector_X, vector_Y))

# Compute vector magnitudes
magnitude_X = sum(x ** 2 for x in vector_X) ** 0.5
magnitude_Y = sum(y ** 2 for y in vector_Y) ** 0.5

# Avoid division by zero and compute cosine similarity
cosine_sim = dot_product / (magnitude_X * magnitude_Y) if magnitude_X and magnitude_Y else 0

# Display results
print("=== Cosine Similarity Result ===")
print(f"Vector X: {vector_X}")
print(f"Vector Y: {vector_Y}")
print(f"Cosine Similarity: {cosine_sim:.4f}")
