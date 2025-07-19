import pandas as pd
file_path = "Lab Session Data.xlsx"
sheet_name = "thyroid0387_UCI"
df = pd.read_excel(file_path, sheet_name=sheet_name)

print("===== First 5 Records =====")
print(df.head())

print("\n===== Feature Metadata =====")
for col in df.columns:
    dtype = df[col].dtype
    unique_count = df[col].nunique()
    print(f"{col}: Data Type = {dtype}, Unique Entries = {unique_count}")

print("\n===== Encoding Recommendations =====")
for col in df.columns:
    if df[col].dtype == 'object':
        print(f"{col}: Consider using One-Hot Encoding")

print("\n===== Summary Stats for Numeric Columns =====")
numeric_cols = df.select_dtypes(include='number').columns
for col in numeric_cols:
    col_data = df[col].dropna()
    print(f"{col} → Min: {col_data.min():.2f}, Max: {col_data.max():.2f}, Mean: {col_data.mean():.2f}, Std Dev: {col_data.std():.2f}")

print("\n===== Missing Value Report =====")
missing_report = df.isnull().sum()
print(missing_report[missing_report > 0] if missing_report.any() else "No missing values detected.")

print("\n===== Outlier Detection using IQR =====")
for col in numeric_cols:
    series = df[col].dropna()
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"{col}: {outliers.shape[0]} outlier(s)")
