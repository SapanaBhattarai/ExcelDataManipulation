import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path, file_format='xlsx'):
    """Load data from an Excel or CSV file."""
    if file_format == 'xlsx':
        return pd.read_excel(file_path)
    elif file_format == 'csv':
        return pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format")

def sort_data(df, sort_by, ascending=True):
    """Sort the DataFrame based on a specific column."""
    return df.sort_values(by=sort_by, ascending=ascending)

def filter_data(df, condition):
    """Filter data based on a condition."""
    return df.query(condition)

def fill_missing_values(df, strategy='mean'):
    """Fill missing values using a specified strategy."""
    if strategy == 'mean':
        return df.fillna(df.mean())
    elif strategy == 'median':
        return df.fillna(df.median())
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    elif strategy == 'drop':
        return df.dropna()
    else:
        raise ValueError("Unsupported strategy")

def transform_data(df, column, func):
    """Apply a function to a specified column."""
    df[column] = df[column].apply(func)
    return df

def aggregate_data(df, group_by_column, agg_func):
    """Aggregate data by a specified column using a given function."""
    return df.groupby(group_by_column).agg(agg_func)

def merge_data(df1, df2, on, how='inner'):
    """Merge two DataFrames based on a common column."""
    return pd.merge(df1, df2, on=on, how=how)

def plot_data(df, x_col, y_col):
    """Plot data to visualize trends."""
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_col], df[y_col], marker='o', linestyle='-', color='b')
    plt.title(f'{y_col} over {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.savefig('data/plot.png')
    plt.show()

def main():
    # File path to the data file
    file_path = 'data/input_data.xlsx'
    
    # Load data
    df = load_data(file_path, file_format='xlsx')
    
    # Sort data by 'Date' column in ascending order
    sorted_df = sort_data(df, sort_by='Date', ascending=True)
    
    # Filter data where 'Score' is greater than 80
    filtered_df = filter_data(sorted_df, 'Score > 80')
    
    # Fill missing values with the mean of the column
    filled_df = fill_missing_values(filtered_df, strategy='mean')
    
    # Transform 'Score' column by applying a lambda function
    transformed_df = transform_data(filled_df, 'Score', lambda x: x * 1.1)
    
    # Aggregate data by 'Name' and calculate the average 'Score'
    aggregated_df = aggregate_data(transformed_df, 'Name', {'Score': 'mean'})
    
    # If you have another dataset to merge
    # other_df = load_data('data/other_data.xlsx', file_format='xlsx')
    # merged_df = merge_data(aggregated_df, other_df, on='Name', how='inner')
    
    # Save the processed data
    aggregated_df.to_excel('data/processed_data.xlsx', index=False)
    
    # Plot data
    plot_data(aggregated_df, 'Name', 'Score')
    
    print("Data processing complete. Results saved to 'data/processed_data.xlsx' and plot saved to 'data/plot.png'.")

if __name__ == "__main__":
    main()
