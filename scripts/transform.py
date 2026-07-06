import pandas as pd

# ------------------------------
# STEP 1: Read the cleaned CSV
# ------------------------------
file_path = r"D:\data engineering project\sales-data-pipeline\data\cleaned\sales_cleaned.csv"
df =pd.read_csv(file_path)
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

print("Cleaned data loaded successfully!")
print(df.head())


# ------------------------------
# STEP 2: Check dataset size
# ------------------------------
print("\nRows and columns:")
print(df.shape)


# ------------------------------
# STEP 3: Chech columns names
# ------------------------------
print("\nColumns:")
print(df.columns)


# ------------------------------
# STEP 4: Create DimCustomer
# ------------------------------
dim_customer = df[["CustomerName","City","State"]]
dim_customer = dim_customer.drop_duplicates()

print("\nDimcustomer:")
print(dim_customer.head())
print("\nDimCustomer shape:")
print(dim_customer.shape)


# ------------------------------
# STEP 5: Add CustomerID
# ------------------------------
dim_customer = dim_customer.reset_index(drop=True)
dim_customer["CustomerID"] = range(1,len(dim_customer)+1)
print("\nDimCustomer:")
print(dim_customer.head())


# ------------------------------
# STEP 6: Reorder CustomerId columns
# ------------------------------
dim_customer= dim_customer[[
    "CustomerID","CustomerName","City", "State"
]]
print(dim_customer.head())


# ------------------------------
# STEP 7: Save DimCustomer
# ------------------------------
output_path = r"D:\data engineering project\sales-data-pipeline\data\warehouse\DimCustomer.csv"
dim_customer.to_csv(output_path, index=False)
print("\nDimCustomer saved successfully!")
print(output_path)


# ------------------------------
# STEP 8: Create DimProduct
# ------------------------------
dim_product = df[["Product","Category"]]
dim_product = dim_product.drop_duplicates()
print(dim_product.head())


# ------------------------------
# STEP 9: Add ProductID
# ------------------------------
dim_product = dim_product.reset_index(drop=True)
dim_product["ProductID"] = range(1,len(dim_product)+1)
print(dim_product.head())


# ------------------------------
# STEP 10: Reorder ProductID columns
# ------------------------------
dim_product= dim_product[[
    "ProductID","Product","Category"
]]
print(dim_product.head())


# ------------------------------
# STEP 11: Save DimProduct
# ------------------------------
output_path=r"D:\data engineering project\sales-data-pipeline\data\warehouse\DimProduct.csv"
dim_product.to_csv(output_path,index=False)


# ------------------------------
# STEP 12: Create DimDate
# ------------------------------
dim_date = df[["OrderDate"]]
dim_date = dim_date.drop_duplicates()
print(dim_date.head())


# ------------------------------
# STEP 13: Adding columns
# ------------------------------
dim_date = dim_date.reset_index(drop=True)
dim_date["DateID"] = range(1 ,len(dim_date)+1)
dim_date["Year"] = dim_date["OrderDate"].dt.year
dim_date["Month"] = dim_date["OrderDate"].dt.month
dim_date["Day"] = dim_date["OrderDate"].dt.day
dim_date["Quarter"] = dim_date["OrderDate"].dt.quarter


# ------------------------------
# STEP 14: Reorder DateID
# ------------------------------
dim_date=dim_date[[
    "DateID","OrderDate","Year","Month","Day","Quarter"
]]
print(dim_date.head())


# ------------------------------
# STEP 15: Save DimDate
# ------------------------------
output_path=r"D:\data engineering project\sales-data-pipeline\data\warehouse\DimDate.csv"
dim_date.to_csv(output_path,index=False)


# ------------------------------
# STEP 16: Create FactSales
# ------------------------------
fact_sales = df[[
    "OrderID",
    "CustomerName",
    "City",
    "State",
    "Product",
    "Category",
    "OrderDate",
    "Quantity",
    "Price",
    "PaymentMethod"
]]

print(fact_sales.head())


# ------------------------------
# STEP 17: Merge CustomerID
# ------------------------------
fact_sales = fact_sales.merge(
    dim_customer,
    on=["CustomerName","City","State"],
    how="left"
)
print(fact_sales.head())


# ------------------------------
# STEP 18: Merge ProductID
# ------------------------------
fact_sales = fact_sales.merge(
    dim_product,
    on=["Product","Category"],
    how="left"
)
print(fact_sales.head())


# ------------------------------
# STEP 19: Merge Dimdate
# ------------------------------
fact_sales = fact_sales.merge(
    dim_date,
    on=["OrderDate"],
    how="left"
)
print(fact_sales.head())



# ------------------------------
# STEP 20: Keep only FactSales columns
# ------------------------------
fact_sales = fact_sales[
    [
        "OrderID",
        "CustomerID",
        "ProductID",
        "DateID",
        "Quantity",
        "Price",
        "PaymentMethod"
    ]
]
print(fact_sales.head())


# ------------------------------
# STEP 20: Save Function
# ------------------------------
output_path=r"D:\data engineering project\sales-data-pipeline\data\warehouse\FactSales.csv"
fact_sales.to_csv(output_path,index=False)

