# e-commerce_sales_data_analysis
To analyze e-commerce sales data and visualize business insights using an interactive Streamlit dashboard. The dashboard provides metrics like total revenue, revenue by category, and top-selling products, helping stakeholders understand product performance and customer behavior.

# 🛒 E-Commerce Sales Analytics Dashboard

An interactive data analytics dashboard built with **Python** and **Streamlit** to visualize and analyze e-commerce sales data from a CSV file.

## 📌 Project Overview

This project helps businesses gain insights into their sales performance by providing key metrics like:
- Total revenue
- Revenue by product category
- Top-selling products

The dashboard is simple, interactive, and ideal for beginners learning data analysis and Streamlit.

---

## 📁 Dataset

Sample data is stored in a CSV file (`data.csv`) with the following columns:

| Column     | Description                     |
|------------|---------------------------------|
| Order ID   | Unique identifier for the order |
| Date       | Date of the order               |
| Customer   | Name of the customer            |
| Category   | Product category (e.g. Fashion, Electronics) |
| Product    | Name of the product             |
| Quantity   | Units sold                      |
| Price      | Price per unit                  |
| Total      | Total amount (Quantity × Price) |

---

## 🛠️ Tech Stack

- **Python 3**
- **Pandas** – data manipulation
- **Streamlit** – dashboard and UI

---

## 🚀 How to Run This Project

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ecommerce-analysis-dashboard.git
cd ecommerce-analysis-dashboard
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Streamlit App
bash
Copy
Edit
streamlit run streamlit_dashboard.py
📊 Features
View basic data info (rows, columns, types)

Calculate total revenue

Analyze revenue by category

Identify top 3 selling products

Simple and clean UI for easy navigation
