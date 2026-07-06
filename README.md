# Sales Data Pipeline

## Project Overview

This project demonstrates a complete beginner-friendly Data Engineering pipeline.

The project includes:

- Extracting sales data from CSV
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
- Git & GitHub

---

## Project Structure

```
sales-data-pipeline/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── warehouse/
│   
├── scripts/
│   ├── extract.py
│   ├── clean.py
│   └── transform.py
│
├── sql/
│   ├── create_tables.sql
│   └── load_data.sql
│
├── dashboard/
│   └── SalesDashboard.pbix
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Data Warehouse

Star Schema:

- FactSales
- DimCustomer
- DimProduct
- DimDate

---

## Power BI Dashboard

Dashboard includes:

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
- Star Schema
- DAX Measures
- Data Visualization
- Dashboard Design

---

## Author

Gaurav Dutta