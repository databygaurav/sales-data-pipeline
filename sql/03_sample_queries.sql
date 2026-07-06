USE sales_data_warehouse;

-- ------------------------------
-- View FactSales
-- ------------------------------
SELECT * FROM FactSales;


-- ------------------------------
-- View DimCustomer
-- ------------------------------
SELECT * FROM DimCustomer;


-- ------------------------------
-- View DimProduct
-- ------------------------------
SELECT * FROM DimProduct;


-- ------------------------------
-- View DimDate
-- ------------------------------
SELECT * FROM DimDate;


-- ------------------------------
-- Customer, Product and Quantity
-- ------------------------------
SELECT
    c.CustomerName,
    p.Product,
    f.Quantity
FROM FactSales AS f
JOIN DimCustomer AS c
    ON f.CustomerID = c.CustomerID
JOIN DimProduct AS p
    ON f.ProductID = p.ProductID;


-- ------------------------------
-- Customer, Product, Date, Quantity and Price
-- ------------------------------
SELECT
    c.CustomerName,
    p.Product,
    d.OrderDate,
    f.Quantity,
    f.Price
FROM FactSales AS f
JOIN DimCustomer AS c
    ON f.CustomerID = c.CustomerID
JOIN DimProduct AS p
    ON f.ProductID = p.ProductID
JOIN DimDate AS d
    ON f.DateID = d.DateID;


-- ------------------------------
-- Total Revenue by Product
-- ------------------------------
SELECT
    p.Product,
    SUM(f.Quantity * f.Price) AS TotalRevenue
FROM FactSales AS f
JOIN DimProduct AS p
    ON f.ProductID = p.ProductID
GROUP BY p.Product;


-- ------------------------------
-- Total Revenue by Payment Method
-- ------------------------------
SELECT
    PaymentMethod,
    COUNT(*) AS NumberOfOrders,
    SUM(Quantity * Price) AS TotalRevenue
FROM FactSales
GROUP BY PaymentMethod;


-- ------------------------------
-- Total Orders by Payment Method
-- ------------------------------
SELECT
    PaymentMethod,
    COUNT(*) AS TotalOrders
FROM FactSales
GROUP BY PaymentMethod;