import statistics as stats

# Stock record entries (hardcoded)
stock_entries = [
    {"date": "Jul 14, 2020", "month": "Jul", "day": "Tue", "price": 1362.15, "chg": -2.52},
    {"date": "Jul 13, 2020", "month": "Jul", "day": "Mon", "price": 1397.35, "chg": -0.26},
    {"date": "Jul 10, 2020", "month": "Jul", "day": "Fri", "price": 1400.95, "chg": 1.15},
    {"date": "Jul 09, 2020", "month": "Jul", "day": "Thu", "price": 1385.05, "chg": -0.36},
    {"date": "Jul 08, 2020", "month": "Jul", "day": "Wed", "price": 1390.10, "chg": -0.52},
    {"date": "Jul 07, 2020", "month": "Jul", "day": "Tue", "price": 1397.40, "chg": -0.24},
    {"date": "Jul 06, 2020", "month": "Jul", "day": "Mon", "price": 1400.75, "chg": -0.31},
    {"date": "Jul 03, 2020", "month": "Jul", "day": "Fri", "price": 1405.10, "chg": -0.51},
    {"date": "Jul 02, 2020", "month": "Jul", "day": "Thu", "price": 1412.35, "chg": 3.62},
    {"date": "Jul 01, 2020", "month": "Jul", "day": "Wed", "price": 1363.05, "chg": 0.32},
]

# Extracting price and change values
price_list = [entry["price"] for entry in stock_entries]
change_list = [entry["chg"] for entry in stock_entries]

# 1. Mean and Variance of All Prices 
avg_price = stats.mean(price_list)
var_price = stats.variance(price_list)

print("=== Price Statistics ===")
print(f"Overall Average Price     : ₹{avg_price:.2f}")
print(f"Price Variance            : {var_price:.2f}")

#  2. Wednesday-Specific Price Analysis 
wed_prices = [rec["price"] for rec in stock_entries if rec["day"] == "Wed"]
wed_avg = stats.mean(wed_prices) if wed_prices else 0
print("\n=== Wednesday Analysis ===")
print(f"Average Price on Wednesdays : ₹{wed_avg:.2f}")
print(f"Deviation from Overall Avg  : {wed_avg - avg_price:.2f}")

# 3. April Month Check
apr_prices = [rec["price"] for rec in stock_entries if rec["month"] == "Apr"]
print("\n=== April Month Data ===")
if apr_prices:
    apr_avg = stats.mean(apr_prices)
    print(f"Mean April Price       : ₹{apr_avg:.2f}")
    print(f"Diff from Overall Mean : {apr_avg - avg_price:.2f}")
else:
    print("No entries found for April.")

# 4. General Loss Probability
loss_count = sum(1 for chg in change_list if chg < 0)
loss_prob = loss_count / len(change_list)
print("\n=== Loss Probability ===")
print(f"Probability of Loss     : {loss_prob:.2%}")

# 5. Wednesday Profit Probability 
wed_changes = [rec["chg"] for rec in stock_entries if rec["day"] == "Wed"]
wed_gains = [chg for chg in wed_changes if chg > 0]
wed_profit_prob = len(wed_gains) / len(wed_changes) if wed_changes else 0
print("\n=== Wednesday Profit Probability ===")
print(f"Probability of Profit on Wednesday : {wed_profit_prob:.2%}")

#  6. Conditional Probability (Profit | Wednesday) 
print(f"Conditional P(Profit | Wednesday) : {wed_profit_prob:.2%}")

#   Basic Text-Based Scatter of Changes 
print("\n=== Day-wise % Change Summary ===")
for rec in stock_entries:
    print(f"{rec['day']:>4} | Change: {rec['chg']:>6.2f}%")
