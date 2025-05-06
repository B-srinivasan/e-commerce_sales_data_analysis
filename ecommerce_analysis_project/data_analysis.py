import pandas as pd

df = pd.read_csv("data/orders.csv")

print("📊 Live Order Summary\n")
print(df.tail(5))  # Show last 5 orders
print("\n💰 Total Revenue:", round(df['Total'].sum(), 2))
print("\n🔥 Top Selling Products:")
print(df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(3))
