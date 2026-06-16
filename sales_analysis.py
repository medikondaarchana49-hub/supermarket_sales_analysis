import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset/supermarket_sales.csv")

# -------------------------------
# 1. Revenue by City
# -------------------------------

sales_by_city = df.groupby("city")["revenue"].sum()

sales_by_city.plot(kind="bar")

plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue")

plt.show()

# -------------------------------
# 2. Payment Method Pie Chart
# -------------------------------

payment_counts = df["payment_method"].value_counts()

payment_counts.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Payment Methods")

plt.ylabel("")

plt.show()

# -------------------------------
# 3. Product Line Revenue
# -------------------------------

product_sales = df.groupby("product_line")["revenue"].sum()

product_sales.plot(kind="bar")

plt.title("Revenue by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.show()

# -------------------------------
# 4. Customer Ratings Histogram
# -------------------------------

plt.hist(df["rating"])

plt.title("Customer Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Customers")

plt.show()

# -------------------------------
# 5. Gender-wise Purchases
# -------------------------------

gender_counts = df["gender_customer"].value_counts()

gender_counts.plot(kind="bar")

plt.title("Gender-wise Customer Purchases")
plt.xlabel("Gender")
plt.ylabel("Number of Purchases")

plt.show()