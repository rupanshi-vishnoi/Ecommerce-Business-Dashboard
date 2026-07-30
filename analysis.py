import pandas as pd

customers = pd.read_csv("data/olist_customers_dataset.csv")

print(customers.head())
import pandas as pd

customers = pd.read_csv("data/olist_customers_dataset.csv")

print(customers.head())

print("\nDataset Shape:")
print(customers.shape)

print("\nColumns:")
print(customers.columns)

print("\nInformation:")
print(customers.info())

print("\nMissing Values:")
print(customers.isnull().sum())
orders = pd.read_csv("data/olist_orders_dataset.csv")

print("\nOrders Dataset")
print(orders.head())

print(orders.shape)
print(orders.info())
print(orders.isnull().sum())
products = pd.read_csv("data/olist_products_dataset.csv")

print(products.head())

print(products.shape)
order_items = pd.read_csv("data/olist_order_items_dataset.csv")

print(order_items.head())
payments = pd.read_csv("data/olist_order_payments_dataset.csv")

print(payments.head())
print("\n===== Missing Values =====")
print(customers.isnull().sum())

print(orders.isnull().sum())

print(products.isnull().sum())

print(order_items.isnull().sum())

print(payments.isnull().sum())
print("\n===== Duplicate Values =====")

print("Customers :", customers.duplicated().sum())
print("Orders :", orders.duplicated().sum())
print("Products :", products.duplicated().sum())
print("Order Items :", order_items.duplicated().sum())
print("Payments :", payments.duplicated().sum())
print("\n===== Dataset Info =====")

print(customers.info())

print(orders.info())

print(products.info())

print(order_items.info())

print(payments.info())
print("\n===== Data Types =====")

print(customers.dtypes)

print(orders.dtypes)

print(products.dtypes)
print("\n===== Summary =====")

print(payments.describe())
customers = customers.drop_duplicates()

orders = orders.drop_duplicates()

products = products.drop_duplicates()

order_items = order_items.drop_duplicates()

payments = payments.drop_duplicates()
print(customers.shape)

print(orders.shape)

print(products.shape)

print(order_items.shape)

print(payments.shape)
import matplotlib.pyplot as plt
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

orders["Month"] = orders["order_purchase_timestamp"].dt.to_period("M")

monthly_orders = orders.groupby("Month").size()

print(monthly_orders)
plt.figure(figsize=(12,5))

monthly_orders.plot()

plt.title("Monthly Orders")
plt.xlabel("Month")
plt.ylabel("Number of Orders")

plt.show()
top_states = customers["customer_state"].value_counts().head(10)

print(top_states)
top_states = customers["customer_state"].value_counts().head(10)

print(top_states)
plt.figure(figsize=(8,5))

top_states.plot(kind="bar")

plt.title("Top 10 Customer States")
plt.xlabel("State")
plt.ylabel("Customers")

plt.show()
customer_orders = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="inner"
)

print(customer_orders.head())
print(customer_orders.shape)
customer_orders = pd.merge(
    customer_orders,
    order_items,
    on="order_id",
    how="inner"
)

print(customer_orders.head())
print(customer_orders.shape)
customer_orders = pd.merge(
    customer_orders,
    products,
    on="product_id",
    how="left"
)

print(customer_orders.head())
print(customer_orders.shape)
customer_orders = pd.merge(
    customer_orders,
    payments,
    on="order_id",
    how="left"
)

print(customer_orders.head())
print(customer_orders.shape)
customer_orders.to_csv("data/final_dataset.csv", index=False)

print("Final Dataset Saved Successfully!")