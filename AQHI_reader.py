import csv
import pandas as pd
import os

# This function converts AQHI data from a CSV file to an Excel file.
def AQHI_reader(csv_file):
    csv_file_name = os.path.basename(csv_file)
    csv_file_date = csv_file_name[:6]

    df = pd.read_csv(csv_file, header=None, usecols=list(range(18)), skiprows=8, na_values=['*'], parse_dates=[0])
    df.columns = ['Date', 'Hour', 'Central/Western', 'Eastern', 'Kwun Tong', 'Sham Shui Po', 'Kwai Chung', 'Tsuen Wan', 'Tseung Kwan O', 'Yuen Long', 'Tuen Mun', 'Tung Chung', 'Tai Po', 'Sha Tin', 'Tap Mun', 'Causeway Bay', 'Central', 'Mong Kok']
    # Remove the time component from the Date column
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    # Drop rows where 'Hour' column contains 'Daily Max'
    df = df[df['Hour'] != 'Daily Max']
    # Calculate the mean of each column and add to DataFrame
    mean_row = df.mean(numeric_only=True).to_frame().T
    mean_row['Date'] = f"{csv_file_date}"
    mean_row['Hour'] = 'Monthly Average'
    df = pd.concat([df, mean_row], ignore_index=True)

    # Write DataFrame to Excel file
    df.to_excel(f'csv_to_excel/AQHI_excel/{csv_file_date}_AQHI.xlsx', index=False)
    print('Excel file generated')

csv_files = [f for f in os.listdir('data/') if f.endswith('.csv')]

# AQHI_reader('data\AQHI_csv/202001_Eng.csv')
# loop through each CSV file and call the AQHI_reader function
for csv_file in csv_files:
    AQHI_reader(f"data/{csv_file}")