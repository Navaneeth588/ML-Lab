import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, RobustScaler

def load_excel_data(file_path, sheet):
    """Load data from a specified Excel sheet."""
    return pd.read_excel(file_path, sheet_name=sheet)

def find_numeric_columns_for_scaling(df):
    """Identify numeric columns with more than two unique values."""
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    return [col for col in numeric_cols if df[col].nunique() > 2]

def detect_outliers_iqr(series):
    """Returns True if outliers exist in the series using IQR."""
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return ((series < lower) | (series > upper)).any()

def scale_numeric_columns(df, columns):
    """Scale numeric columns using RobustScaler or MinMaxScaler."""
    scaled_df = df.copy()
    applied_methods = {}

    for column in columns:
        non_null_series = df[column].dropna()

        if detect_outliers_iqr(non_null_series):
            scaler = RobustScaler()
            method = "RobustScaler (resistant to outliers)"
        else:
            scaler = MinMaxScaler()
            method = "MinMaxScaler (0–1 normalization)"

        reshaped_values = df[[column]].values  # 2D array for sklearn
        scaled_df[column] = scaler.fit_transform(reshaped_values)
        applied_methods[column] = method

    return scaled_df, applied_methods

def process_and_normalize():
    path = "Lab Session Data.xlsx"
    sheet_name = "thyroid0387_UCI"

    data = load_excel_data(path, sheet_name)
    columns_to_scale = find_numeric_columns_for_scaling(data)

    print("📊 Columns selected for normalization:")
    print(columns_to_scale)

    normalized_df, methods_used = scale_numeric_columns(data, columns_to_scale)

    print("\n⚙️ Normalization methods applied:")
    for col, method in methods_used.items():
        print(f"{col}: {method}")

    return normalized_df

if __name__ == "__main__":
    final_scaled_data = process_and_normalize()
