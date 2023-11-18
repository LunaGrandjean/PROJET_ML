import pandas as pd


def clean_and_transform_data(df):
    """Clean and transform the DataFrame by removing specific columns, converting categorical data to numerical, 
    adding new columns based on existing data, and calculating cumulative counts.

    This function performs the following operations:
    - Removes unnecessary columns ('Line' and 'Official Top').
    - Converts 'Gender' to numerical values (M=1, F=0).
    - Converts 'Discipline' to numerical values based on unique disciplines present in the data {'FIM': 0, 'CNF': 1, 'CWT': 2, 'CWTB': 3}.
    - Adds a 'Month' column extracted from the 'Day' column.
    - Calculates the cumulative count of dives per diver as 'Experience Dive'.
    - Calculates the cumulative count of dives per diver per discipline as 'Experience Discipline'.

    Args:
        df (DataFrame): The DataFrame to be cleaned and transformed.
    
    Returns:
        DataFrame: The cleaned and transformed DataFrame.
    """

    # Remove 'Line' and 'Official Top' columns
    df.drop(columns=['Line', 'Official Top'], inplace=True)

    # Convert 'Gender' to numerical values (M=1, F=0)
    gender_to_int = {'M': 1, 'F': 0}
    df['Gender'] = df['Gender'].map(gender_to_int)

    # Convert 'Discipline' to numerical values
    disciplines = df['Discipline'].unique()
    discipline_to_int = {disc: idx for idx, disc in enumerate(disciplines)}
    df['Discipline'] = df['Discipline'].map(discipline_to_int)

    # Add 'Month' column extracted from 'Day'
    df['Month'] = pd.to_datetime(df['Day']).dt.month

    # Calculate general diving experience
    df['Experience Dive'] = df.groupby('Diver').cumcount()

    # Calculate diving experience in each discipline
    df['Experience Discipline'] = df.groupby(['Diver', 'Discipline']).cumcount()

    return df


def clean_data(df):
    """Clean the DataFrame by replacing unexploitable values with NaN and removing rows with missing values.

    This function performs the following operations:
    - Replaces specified unexploitable values like '()', empty strings, and spaces with NaN.
    - Removes all rows that have any missing values (NaN).

    Args:
        df (DataFrame): The DataFrame to be cleaned.
    
    Returns:
        DataFrame: The cleaned DataFrame.
    """
    import numpy as np

    # Replace unexploitable values with NaN
    df.replace({'()': np.nan, '': np.nan, ' ': np.nan}, inplace=True)

    # Remove all rows with missing values
    df_cleaned = df.dropna()

    return df_cleaned

def save_cleaned_data(df, file_path='your_cleaned_file.csv'):
    """Save the cleaned DataFrame to a CSV file.

    Args:
        df (DataFrame): The DataFrame to be saved.
        file_path (str): The file path to save the DataFrame.
    """
    df.to_csv(file_path, index=False)