# Sales Data Pipeline

## Project Overview

This project demonstrates a complete beginner-friendly Data Engineering pipeline.

The project includes:

- Extracting sales data from a CSV file
- Cleaning missing values using Python (Pandas)
- Transforming the data into a Star Schema
- Loading the data into MySQL
- Creating an interactive dashboard in Power BI

---

## Technologies Used

- Python
- Pandas
- MySQL
- SQL
- Power BI
- Git
- GitHub

---

## Project Structure

```text
sales-data-pipeline/
│
├── dashboard/
│   └── SalesDashboard.pbix
│
├── data/
│   ├── raw/
│   │   └── sales.csv
│   ├── cleaned/
│   │   └── sales_cleaned.csv
│   └── warehouse/
│       ├── DimCustomer.csv
│       ├── DimDate.csv
│       ├── DimProduct.csv
│       └── FactSales.csv
│
├── scripts/
│   ├── extract.py
│   ├── clean.py
│   └── transform.py
│
├── sql/
│   ├── 01_create_database.sql
│   ├── 02_create_tables.sql
│   └── 03_sample_queries.sql
│
├── README.md
└── .gitignore
```

---

## Data Warehouse

This project uses a **Star Schema** consisting of:

- FactSales
- DimCustomer
- DimProduct
- DimDate

---

## Power BI Dashboard

The dashboard includes:

- Total Revenue KPI
- Total Orders KPI
- Total Customers KPI
- Total Products KPI
- Revenue by Product
- Revenue by Month
- Revenue by State
- Orders by Payment Method
- Product Filter
- State Filter
- Year Filter

---

## Skills Demonstrated

- Data Cleaning
- ETL Pipeline
- Data Modeling
- SQL Joins
- Star Schema Design
- DAX Measures
- Power BI Dashboard Development
- Data Visualization
- Git & GitHub

---

## Author

**Gaurav Dutta**
