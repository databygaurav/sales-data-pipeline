USE sales_data_warehouse;

-- ------------------------------
-- Create DimCustomer
-- ------------------------------
CREATE TABLE DimCustomer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(100),
    State VARCHAR(100)
);


-- ------------------------------
-- Create DimProduct
-- ------------------------------
CREATE TABLE DimProduct (
    ProductID INT PRIMARY KEY,
    Product VARCHAR(100),
    Category VARCHAR(100)
);


-- ------------------------------
-- Create DimDate
-- ------------------------------
CREATE TABLE DimDate (
    DateID INT PRIMARY KEY,
    OrderDate DATE,
    Year INT,
    Month INT,
    Day INT,
    Quarter INT
);


-- ------------------------------
-- Create FactSales
-- ------------------------------
CREATE TABLE FactSales (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    DateID INT,
    Quantity INT,
    Price DECIMAL(10,2),
    PaymentMethod VARCHAR(100),

    FOREIGN KEY (CustomerID) REFERENCES DimCustomer(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES DimProduct(ProductID),
    FOREIGN KEY (DateID) REFERENCES DimDate(DateID)
);