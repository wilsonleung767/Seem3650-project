import pandas as pd
import os
from openpyxl import load_workbook


def windspeed_reader(file):
    # Read the second row of the CSV file to get the place name
    place_row = pd.read_csv(file, nrows=1, skiprows=[0], header=None )
    place_name = str(place_row.iloc[0, 0]).split(' - ')[-1]

    # Read the data starting from the fourth row of the CSV file into a DataFrame
    df = pd.read_csv(file, skiprows=2,skipfooter=4, engine='python')

    # Rename the columns to English names
    df.columns = ['Year', 'Month', 'Day', 'Value', 'Data Completeness']
    
    # Drop all data before 2020
    df = df[df['Year'] >= 2020 ]
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

    # Calculate the monthly average of the 'Value' column
    monthly_avg = df.groupby(['Year', 'Month'])['Value'].mean().reset_index()
    monthly_avg = monthly_avg.sort_values(['Year', 'Month'])
    avg = df["Value"]
    print(avg)
    
    # Write the monthly average to a new Excel file starting from cell B2
    with pd.ExcelWriter(f'csv_to_excel/copydata{place_name}.xlsx') as writer:
        monthly_avg.to_excel(writer, sheet_name='Sheet1', index=False)

    # Merge the monthly average with the original DataFrame
    df = pd.merge(df, monthly_avg, on=['Year', 'Month'])
    
    # Rename the new column to 'Monthly Avg'
    df.rename(columns={'Value_y': 'Monthly Avg'}, inplace=True)


    # Reset the index and drop the original index column
    df = df.reset_index(drop=True)

    # Save the DataFrame to an Excel file named after the place
    filename = f'csv_to_excel/WindSpeed_excel/{place_name}_humidity.xlsx'
    df.to_excel(filename)

def process_files_in_folder(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Process each file one by one
    for file in files:
        # Skip any files that are not CSV files
        if not file.endswith('.csv') or ('2023' in file):
            continue

        # Process the CSV file
        file_path = os.path.join(folder_path, file)
        windspeed_reader(file_path)
    print("Completed")


windspeed_reader('Raw_data\WindSpeed\daily__NP_ALL.csv')
# process_files_in_folder("Raw_data\WindSpeed")