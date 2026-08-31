import pandas as pd
import os

# Function to inspect and process the file
def inspect_csv(filename):
    try:
        # Detect file type
        if filename.endswith(".tsv"):
            df = pd.read_csv(filename, sep="\t")
        else:
            df = pd.read_csv(filename)

        print("\n========== CSV FILE INSPECTOR ==========")

        # Display first 5 rows
        print("\nFirst 5 Rows:")
        print(df.head())

        # Display number of rows and columns
        rows, columns = df.shape
        print("\nFile Dimensions:")
        print("Rows    :", rows)
        print("Columns :", columns)

        # Display column names
        print("\nColumn Names:")
        print(df.columns.tolist())

        # Display data types
        print("\nData Types:")
        print(df.dtypes)

        # Check missing values
        print("\nMissing Values:")
        print(df.isnull().sum())

        # Display statistical summary for numerical columns
        print("\nNumerical Summary:")
        print(df.describe())

        # Ask user for filtering condition
        print("\n========== FILTER DATA ==========")
        print("Available columns:")
        print(df.columns.tolist())

        column = input("Enter column name for filtering: ")

        if column not in df.columns:
            print("Column does not exist.")
            return

        value = float(input("Enter minimum value: "))

        # Filter rows
        filtered_df = df[df[column] >= value]

        print("\nFiltered Data:")
        print(filtered_df)

        # Export filtered data
        output_file = "filtered_data.csv"
        filtered_df.to_csv(output_file, index=False)

        print("\nFiltered data successfully exported!")
        print("Output file:", output_file)

        # Also export as TSV
        tsv_file = "filtered_data.tsv"
        filtered_df.to_csv(tsv_file, sep="\t", index=False)

        print("TSV file successfully exported!")
        print("Output file:", tsv_file)

    except FileNotFoundError:
        print("Error: File not found.")

    except ValueError:
        print("Error: Please enter a valid numerical value.")

    except Exception as e:
        print("An error occurred:", e)


# Main program
print("Automated CSV File Inspector and Data Exporter")

filename = input("Enter CSV/TSV file name: ")

inspect_csv(filename)