import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

def read_data_subset(path, sheet, rows=20):
    """Reads the top `rows` entries from the specified Excel sheet."""
    return pd.read_excel(path, sheet_name=sheet).iloc[:rows]

def extract_binary_features(dataframe):
    """Identify binary features (with only 0 and 1 as values)."""
    binary_cols = []
    for col in dataframe.columns:
        unique_vals = dataframe[col].dropna().unique()
        if set(unique_vals).issubset({0, 1}):
            binary_cols.append(col)
    return binary_cols

def calculate_jaccard_and_smc(dataframe):
    """Compute Jaccard and Simple Matching Coefficient matrices."""
    bin_features = extract_binary_features(dataframe)
    bin_data = dataframe[bin_features]

    obs = bin_data.shape[0]
    jaccard = np.zeros((obs, obs))
    smc = np.zeros((obs, obs))

    for i in range(obs):
        for j in range(obs):
            a = bin_data.iloc[i]
            b = bin_data.iloc[j]
            match_11 = ((a == 1) & (b == 1)).sum()
            match_00 = ((a == 0) & (b == 0)).sum()
            mismatch_10 = ((a == 1) & (b == 0)).sum()
            mismatch_01 = ((a == 0) & (b == 1)).sum()

            union = match_11 + mismatch_10 + mismatch_01
            total = match_11 + match_00 + mismatch_10 + mismatch_01

            jaccard[i, j] = match_11 / union if union else 0
            smc[i, j] = (match_11 + match_00) / total if total else 0

    return jaccard, smc

def cosine_similarity_matrix(dataframe):
    """Compute cosine similarity matrix for numeric columns."""
    numeric_part = dataframe.select_dtypes(include=[np.number])
    return cosine_similarity(numeric_part)

def draw_similarity_heatmap(similarity_data, heading):
    """Generate and show a heatmap from similarity data."""
    plt.figure(figsize=(9, 7))
    sns.heatmap(similarity_data, annot=True, fmt=".2f", cmap="YlGnBu", square=True,
                cbar_kws={'label': 'Similarity'})
    plt.title(heading)
    plt.xlabel("Index")
    plt.ylabel("Index")
    plt.tight_layout()
    plt.show()

def run_similarity_analysis():
    file = "Lab Session Data.xlsx"
    sheet = "thyroid0387_UCI"

    df = read_data_subset(file, sheet)

    print("[1] Computing binary feature similarity (Jaccard & SMC)...")
    jac, smc = calculate_jaccard_and_smc(df)

    print("[2] Computing cosine similarity for numeric attributes...")
    cos = cosine_similarity_matrix(df)

    print("[3] Displaying similarity heatmaps...")
    draw_similarity_heatmap(jac, "Jaccard Similarity (Top 20 Rows)")
    draw_similarity_heatmap(smc, "Simple Matching Coefficient (Top 20 Rows)")
    draw_similarity_heatmap(cos, "Cosine Similarity (Top 20 Rows)")

# Run the analysis if this script is executed directly
if __name__ == "__main__":
    run_similarity_analysis()
