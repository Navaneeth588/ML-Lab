import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Sample shopping data
transactions = {
    'Candy_Units': [20, 16, 27, 19, 24, 22, 15, 18, 21, 16],
    'Mango_Weight': [6, 3, 6, 1, 4, 1, 4, 4, 1, 2],
    'Milk_Packs': [2, 6, 2, 2, 2, 5, 2, 2, 4, 4],
    'Total_Bill': [386, 289, 393, 110, 280, 167, 271, 274, 148, 198]
}

# Creating the DataFrame
df_customers = pd.DataFrame(transactions)

# Creating binary labels based on bill amount
def categorize_customer(amount):
    return 'AFFLUENT' if amount > 200 else 'BUDGET'

df_customers['Spending_Type'] = df_customers['Total_Bill'].map(categorize_customer)

# Extracting inputs and labels
input_data = df_customers[['Candy_Units', 'Mango_Weight', 'Milk_Packs']].values
labels = np.array([1 if label == 'AFFLUENT' else 0 for label in df_customers['Spending_Type']])

# Initializing and fitting logistic regression model
log_model = LogisticRegression()
log_model.fit(input_data, labels)

# Predicting outcomes
results = log_model.predict(input_data)
df_customers['Predicted_Type'] = ['AFFLUENT' if res else 'BUDGET' for res in results]

# Output metrics
print("=== Customer Classification Metrics ===")
print(classification_report(labels, results, target_names=['BUDGET', 'AFFLUENT']))
print(f"Prediction Accuracy: {accuracy_score(labels, results):.2f}")

# Final DataFrame display
print("\n=== Final Report ===")
print(df_customers[['Candy_Units', 'Mango_Weight', 'Milk_Packs', 'Total_Bill', 'Spending_Type', 'Predicted_Type']])
