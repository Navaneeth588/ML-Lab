import pandas as pd
import numpy as np

def fetch_excel_data(path, sheet):
    """Import data from an Excel sheet."""
    return pd.read_excel(path, sheet_name=sheet)

def detect_outlier_iqr(series):
    """Use the IQR rule to check for presence of outliers."""
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr_range = q3 - q1
    min_limit = q1 - 1.5 * iqr_range
    max_limit = q3 + 1.5 * iqr_range
    return any((series < min_limit) | (series > max_limit))

def fill_missing_values(dataframe):
    """Handle missing values using mode, median, or mean based on column type and outliers."""
    filled_df = dataframe.copy()

    for column in dataframe.columns:
        if dataframe[column].isnull().sum() == 0:
            continue  # Skip if no missing data

        if dataframe[column].dtype == object:
            # Categorical column → fill with most frequent value
            most_common = dataframe[column].mode().iloc[0]
            filled_df[column] = filled_df[column].fillna(most_common)

        elif np.issubdtype(dataframe[column].dtype, np.number):
            # Numerical column → use mean or median
            col_clean = dataframe[column].dropna()
            if detect_outlier_iqr(col_clean):
                med = col_clean.median()
                filled_df[column] = filled_df[column].fillna(med)
                print(f"[MEDIAN] {column} had outliers, filled using median.")
            else:
                avg = col_clean.mean()
                filled_df[column] = filled_df[column].fillna(avg)
                print(f"[MEAN] {column} had no outliers, filled using mean.")

    return filled_df

def run_imputation():
    file_path = "Lab Session Data.xlsx"
    worksheet = "thyroid0387_UCI"

    original_data = fetch_excel_data(file_path, worksheet)

    print("🔎 Null values BEFORE imputation:\n", original_data.isnull().sum())

    cleaned_data = fill_missing_values(original_data)

    print("\n✅ Null values AFTER imputation:\n", cleaned_data.isnull().sum())

if __name__ == "__main__":
    run_imputation()
