import pandas as pd
import numpy as np

# Function to fill missing values


def fill_missing_values(df):
    # Fill missing 'Name' values with 'Unknown'
    df['Name'].fillna('Unknown', inplace=True)

    # Fill missing 'Salary' with the mean salary
    df['Salary'].fillna(int(df['Salary'].mean()), inplace=True)

    # Fill missing 'Number' with 0 (or another placeholder like 'Not Available')
    df['Number'].fillna(0, inplace=True)

    # Fill missing 'Favorite Food' with 'Not Provided'
    df['Favorite Food'].fillna('Not Provided', inplace=True)

    # Fill missing 'Work Type' with 'Hybrid' (default balanced option)
    df['Work Type'].fillna('Hybrid', inplace=True)

    # Fill missing 'Role' with 'Software Engineer' (default role)
    df['Role'].fillna('Software Engineer', inplace=True)

    return df

# Load the dataset from an Excel file


def load_dataset(file_name):
    df = pd.read_excel(file_name)
    return df

# Save the processed dataset to a new Excel file


def save_dataset(df, output_file_name="processed_dataset_practical_2.xlsx"):
    df.to_excel(output_file_name, index=False)
    print(f"\nProcessed data saved to {output_file_name}")

# Display the processed dataset


def display_dataset(df):
    print("\nProcessed Data:\n")
    print(df)

# Main function to run the program


def main():
    # Load the dataset
    file_name = "practical_2_dataset.xlsx"
    df = load_dataset(file_name)

    # Display original dataset
    print("Original Dataset:")
    print(df)

    # Fill missing values
    df_filled = fill_missing_values(df)

    # Display and save the processed dataset
    display_dataset(df_filled)
    save_dataset(df_filled)


if __name__ == "__main__":
    main()
