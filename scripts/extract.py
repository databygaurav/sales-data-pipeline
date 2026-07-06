import pandas as pd


def extract_data(file_path):
    """
    Read raw sales data from a CSV file.
    """
    df = pd.read_csv(file_path)
    return df


def main():
    # Path to raw dataset
    file_path = r"D:\data engineering project\sales-data-pipeline\data\raw\sales.csv"

    # Extract data
    df = extract_data(file_path)

    # Basic inspection
    print("=" * 50)
    print("SALES DATA EXTRACTION")
    print("=" * 50)

    print(f"\nDataset Shape: {df.shape}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nDataset Information:")
    df.info()

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nExtraction completed successfully!")


if __name__ == "__main__":
    main()