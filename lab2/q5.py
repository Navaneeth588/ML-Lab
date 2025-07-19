# Original numeric feature vectors
vector_A = [20, 6, 2, 386]
vector_B = [16, 3, 6, 289]

# Thresholds for binary conversion (based on domain knowledge)
cutoffs = [18, 4, 3, 300]

# Convert to binary based on thresholds
binary_A = [1 if val > cutoffs[i] else 0 for i, val in enumerate(vector_A)]
binary_B = [1 if val > cutoffs[i] else 0 for i, val in enumerate(vector_B)]

# Initialize counters for comparison outcomes
both_ones = only_A = only_B = both_zeros = 0

for i in range(len(binary_A)):
    a, b = binary_A[i], binary_B[i]
    if a == 1 and b == 1:
        both_ones += 1
    elif a == 1 and b == 0:
        only_A += 1
    elif a == 0 and b == 1:
        only_B += 1
    else:
        both_zeros += 1

# Compute similarity coefficients
jaccard_coeff = both_ones / (both_ones + only_A + only_B) if (both_ones + only_A + only_B) else 0
simple_match = (both_ones + both_zeros) / (both_ones + only_A + only_B + both_zeros) if (both_ones + only_A + only_B + both_zeros) else 0

# Final output
print("=== Binary Representation ===")
print(f"Vector A: {binary_A}")
print(f"Vector B: {binary_B}")

print("\n=== Similarity Measures ===")
print(f"Jaccard Coefficient     : {jaccard_coeff:.4f}")
print(f"Simple Matching Coef.   : {simple_match:.4f}")
