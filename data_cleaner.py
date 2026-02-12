"""
Python Data Cleaning Basics
A beginner-friendly script to clean and process CSV data
"""

import pandas as pd
import os


def load_data(filepath):
    """Load CSV file into a pandas DataFrame"""
    print(f" Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    print(f"✓ Loaded {len(df)} rows and {len(df.columns)} columns\n")
    return df


def display_data_info(df, stage="Initial"):
    """Display basic information about the dataset"""
    print(f"{'='*50}")
    print(f"{stage} Data Summary")
    print(f"{'='*50}")
    print(f"Shape: {df.shape}")
    print(f"\nColumn names and types:")
    print(df.dtypes)
    print(f"\nMissing values per column:")
    print(df.isnull().sum())
    print(f"{'='*50}\n")


def clean_missing_values(df, strategy="drop"):
    """
    Clean missing values from the dataset
    
    Args:
        df: pandas DataFrame
        strategy: 'drop' to remove rows with missing values,
                 'fill' to fill with appropriate values
    """
    print("🧹 Cleaning missing values...")
    
    if strategy == "drop":
        # Remove rows with any missing values
        cleaned_df = df.dropna()
        removed = len(df) - len(cleaned_df)
        print(f"✓ Removed {removed} rows with missing values")
        
    elif strategy == "fill":
        cleaned_df = df.copy()
        # Fill numeric columns with mean
        numeric_cols = cleaned_df.select_dtypes(include=['number']).columns
        for col in numeric_cols:
            if cleaned_df[col].isnull().any():
                cleaned_df[col].fillna(cleaned_df[col].mean(), inplace=True)
                print(f"✓ Filled {col} with mean value")
        
        # Fill text columns with 'Unknown'
        text_cols = cleaned_df.select_dtypes(include=['object']).columns
        for col in text_cols:
            if cleaned_df[col].isnull().any():
                cleaned_df[col].fillna('Unknown', inplace=True)
                print(f"✓ Filled {col} with 'Unknown'")
    
    print()
    return cleaned_df


def remove_duplicates(df):
    """Remove duplicate rows from the dataset"""
    print(" Checking for duplicates...")
    initial_count = len(df)
    cleaned_df = df.drop_duplicates()
    removed = initial_count - len(cleaned_df)
    
    if removed > 0:
        print(f"✓ Removed {removed} duplicate rows\n")
    else:
        print("✓ No duplicates found\n")
    
    return cleaned_df


def sort_data(df, column_name, ascending=True):
    """Sort the dataset by a specified column"""
    if column_name not in df.columns:
        print(f"  Column '{column_name}' not found. Available columns: {list(df.columns)}")
        return df
    
    print(f"📊 Sorting data by '{column_name}' ({'ascending' if ascending else 'descending'})...")
    sorted_df = df.sort_values(by=column_name, ascending=ascending)
    print("✓ Data sorted\n")
    return sorted_df


def save_data(df, output_filepath):
    """Save the cleaned DataFrame to a CSV file"""
    print(f"💾 Saving cleaned data to {output_filepath}...")
    df.to_csv(output_filepath, index=False)
    print(f"✓ Successfully saved {len(df)} rows\n")


def main():
    """Main function to run the data cleaning pipeline"""
    print("\n" + "="*50)
    print(" PYTHON DATA CLEANING BASICS")
    print("="*50 + "\n")
    
    # Configuration
    input_file = "sample_data.csv"
    output_file = "cleaned_data.csv"
    sort_column = "age"  # Change this to match your data
    
    # Create sample data if input file doesn't exist
    if not os.path.exists(input_file):
        print(" Creating sample dataset for demonstration...\n")
        sample_data = {
            'name': ['Alice', 'Bob', None, 'David', 'Eve', 'Bob', 'Frank'],
            'age': [25, 30, 35, None, 28, 30, 45],
            'city': ['New York', 'Paris', 'London', 'Tokyo', None, 'Paris', 'Berlin'],
            'salary': [50000, 60000, 75000, 80000, 55000, 60000, None]
        }
        pd.DataFrame(sample_data).to_csv(input_file, index=False)
        print(f"✓ Created {input_file}\n")
    
    # Step 1: Load data
    df = load_data(input_file)
    
    # Step 2: Display initial data info
    display_data_info(df, "Initial")
    
    # Step 3: Clean missing values
    # Change strategy to 'fill' if you want to fill instead of drop
    df_cleaned = clean_missing_values(df, strategy="drop")
    
    # Step 4: Remove duplicates
    df_cleaned = remove_duplicates(df_cleaned)
    
    # Step 5: Sort data
    if sort_column in df_cleaned.columns:
        df_cleaned = sort_data(df_cleaned, sort_column, ascending=True)
    
    # Step 6: Display final data info
    display_data_info(df_cleaned, "Final")
    
    # Step 7: Save cleaned data
    save_data(df_cleaned, output_file)
    
    print("="*50)
    print(" Data cleaning complete!")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()
