import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="E-commerce Dashboard", layout="wide")

st.title("📦 Real-Time E-commerce Dashboard")

# Autorefresh every 5 seconds
st.caption("Auto-refreshes every 5 seconds.")
placeholder = st.empty()

while True:
    df = pd.read_csv("data/orders.csv")

    with placeholder.container():
        st.subheader("🧾 Latest Orders")
        st.dataframe(df.tail(5), use_container_width=True)

        st.metric("💰 Total Revenue", f"${df['Total'].sum():,.2f}")

        st.subheader("📊 Revenue by Category")
        revenue_by_category = df.groupby("Category")["Total"].sum().sort_values(ascending=False)
        st.bar_chart(revenue_by_category)

        st.subheader("🔥 Top Selling Products")
        top_products = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5)
        st.table(top_products)

    time.sleep(5)
