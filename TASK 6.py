import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("C:\\Users\\Admin\\OneDrive\\TASK 6.xlsx",sheet_name="Dataset")

#total revenue
print("\nTotal_Revenue\n",df["Revenue"].sum())

#Revenue by Product
print("\nRevenue_by_product\n",df.groupby("Product")["Revenue"].sum().sort_values(ascending=False))

#Revenue by City
print("\nRevenue_by_City\n",df.groupby("City")["Revenue"].sum().sort_values(ascending=False))

#Visualization

df.groupby("Product")["Revenue"].sum().plot(kind="bar")
plt.title("Revenue by Product")
plt.show()

df.groupby("Category")["Revenue"].sum().plot(kind="pie")
plt.title("Revenue by Category")
plt.show()
