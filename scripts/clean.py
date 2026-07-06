import pandas as pd 

#------------------------------
# STEP 1: Read the csv file
#------------------------------
file_path= r"D:\data engineering project\sales-data-pipeline\data\raw\sales.csv"
df=pd.read_csv(file_path)
print("Data loaded successfully!")
print(df.head())



#------------------------------
# STEP 2: check dataset size
#------------------------------
print("\nRows and columns:")
print(df.shape)



#------------------------------
# STEP 3: Remove  duplicate rows
#------------------------------
df = df.drop_duplicates()
print("\nRows and columns:")
print(df.shape)



#------------------------------
# STEP 4: Check missing values
#------------------------------
print("\nmissing values in each column:")
print(df.isnull().sum())



#------------------------------
# STEP 5: Fill missing customerNames, State, City, PaymentMethod
#------------------------------
columns = ["CustomerName", "City", "State", "PaymentMethod"]
for column in columns:
    df[column] =df[column].fillna("Unknown")

for column in columns:
    print("\n")
    print(column)
    print(df[column].isnull().sum())



#------------------------------
# STEP 6: Removing invalid Quantity rows 
#------------------------------
df = df[df["Quantity"].notna()]
df = df[df["Quantity"]>0]



# ------------------------------
# STEP 7: Remove invalid Price rows
# ------------------------------
df = df[df["Price"].notna()]
df = df[df["Price"] > 0]

print("\nRows and columns after cleaning Quantity and Price:")
print(df.shape)



# ------------------------------
# STEP 8: Convert orderDate to datetime
# ------------------------------
df["OrderDate"] = pd.to_datetime(df["OrderDate"],dayfirst=True, errors="coerce")
print("\nMissing/Invaild OrderDate:")
print(df["OrderDate"].isnull().sum())



# ------------------------------
# STEP 9: Remove invalid OrderDate
# ------------------------------
df = df.dropna(subset=["OrderDate"])
print("\nRows after removing invalid OrderDate:")
print(df.shape)



# ------------------------------
# STEP 10: Standardize Product names
# ------------------------------
df["Product"] = df["Product"].str.strip().str.title()
print(df["Product"].unique())


#-----------FIANL OUTPUT-------------#
print("\nFinal cleaned dataset shape:")
print(df.shape)



# ------------------------------
# STEP 10: Save cleaned data
# ------------------------------
output_path = r"D:\data engineering project\sales-data-pipeline\data\cleaned\sales_cleaned.csv"
df.to_csv(output_path, index=False)
print("\nCleaned data saved successfully")
print(output_path)