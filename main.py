import pandas as pd

def load_csv(file_path):
    """
    Load CSV file and return a DataFrame.
    Handles file not found or other errors.
    """
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            print(f"{file_path} is empty.")
        else:
            print(f"CSV '{file_path}' loaded successfully!")
        return df
    except FileNotFoundError:
        print(f"{file_path} not found.")
        return None
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

def show_summary(df):
    """
    Display summary statistics and total row count.
    Includes numeric and non-numeric columns.
    """
    print("\nSummary Statistics:")
    print(df.describe(include='all'))  # 'include=all' shows all columns
    print(f"\nTotal rows: {len(df)}")

def filter_data(df):
    """
    Filter the DataFrame by a chosen column and value.
    Allows case-insensitive column input.
    Supports numeric conversion for numeric columns.
    Exports filtered data if requested.
    """
    print(f"\nAvailable columns: {', '.join(df.columns)}")
    
    # Get column input from user
    column_input = input("Enter column to filter by: ")
    
    # Match user input to actual column ignoring case
    column = next((col for col in df.columns if col.lower() == column_input.lower()), None)
    if column is None:
        print("Invalid column name. Try again.")
        return

    # Get value to filter
    value = input(f"Enter value to filter {column} by: ")

    # Convert value to float if column is numeric
    if pd.api.types.is_numeric_dtype(df[column]):
        try:
            value = float(value)
        except ValueError:
            print("Invalid numeric value. Try again.")
            return

    # Filter the DataFrame
    filtered_df = df[df[column] == value]
    print("\nFiltered Data:")
    print(filtered_df)

    # Ask user if they want to export filtered data
    export = input("Do you want to export filtered data? (y/n): ")
    if export.lower() == 'y':
        filtered_df.to_csv('filtered_data.csv', index=False)
        print("Filtered data exported to filtered_data.csv")

def main():
    """
    Main function to run the CSV Data Manager program.
    Displays a menu for user to choose actions repeatedly.
    """
    df = load_csv("data.csv")  # Load CSV file
    if df is None:
        return  # Exit if file not found or error

    while True:
        # Display menu
        print("\n--- CSV Data Manager ---")
        print("1. View first 5 rows")
        print("2. Show summary statistics")
        print("3. Filter data and export")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        # Execute chosen option
        if choice == "1":
            print("\nFirst 5 rows:")
            print(df.head())
        elif choice == "2":
            show_summary(df)
        elif choice == "3":
            filter_data(df)
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1-4.")

# Run program
if __name__ == "__main__":
    main()
