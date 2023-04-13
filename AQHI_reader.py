import csv
import pandas as pd
import os

# This function converts AQHI data from a CSV file to an Excel file.
def AQHI_reader(csv_file):
    csv_file_name = os.path.basename(csv_file)
    csv_file_date = csv_file_name[:6]

    df = pd.read_csv(csv_file, header=None, usecols=[0,1] + list(range(3,19)), skiprows=8, na_values=['*'], parse_dates=[0])
    df.columns = ['Date', 'Hour', 'Central/Western', 'Eastern', 'Kwun Tong', 'Sham Shui Po', 'Kwai Chung', 'Tsuen Wan', 'Tseung Kwan O', 'Yuen Long', 'Tuen Mun', 'Tung Chung', 'Tai Po', 'Sha Tin', 'Tap Mun', 'Causeway Bay', 'Central', 'Mong Kok']
    # Remove the time component from the Date column
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df.to_excel(f'csv_to_excel/{csv_file_date}_AQHI.xlsx', index=False)
    print('Excel file generated')

AQHI_reader('data/202201_Eng.csv')