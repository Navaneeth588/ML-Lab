import numpy as np

# Item quantities for each transaction
item_matrix = np.array([
    [20, 6, 2],
    [16, 3, 6],
    [27, 6, 2],
    [19, 1, 2],
    [24, 4, 2],
    [22, 1, 5],
    [15, 4, 2],
    [18, 4, 2],
    [21, 1, 4],
    [16, 2, 4]
])

# Corresponding total payment for each transaction
payment_vector = np.array([
    [386],
    [289],
    [393],
    [110],
    [280],
    [167],
    [271],
    [274],
    [148],
    [198]
])

# Dimensions
num_items = item_matrix.shape[1]
num_records = item_matrix.shape[0]

# Rank of item matrix
_, s_vals, _ = np.linalg.svd(item_matrix)
effective_rank = np.sum(s_vals > 1e-10)

# Using pseudo-inverse to estimate item costs
pinv_matrix = np.linalg.pinv(item_matrix)
estimated_prices = pinv_matrix @ payment_vector

# Display results
print("======= ANALYSIS SUMMARY =======")
print(f"Total unique items considered  : {num_items}")
print(f"Number of purchase records     : {num_records}")
print(f"Rank of the item matrix (A)    : {effective_rank}\n")

print("Estimated unit prices:")
print(f"• Candy (1 unit)       : ₹{estimated_prices[0][0]:.2f}")
print(f"• Mango (1 kg)         : ₹{estimated_prices[1][0]:.2f}")
print(f"• Milk Packet (1 unit) : ₹{estimated_prices[2][0]:.2f}")
