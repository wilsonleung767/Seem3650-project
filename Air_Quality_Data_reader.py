import csv
import pandas as pd
import os

# https://cd.epic.epd.gov.hk/EPICDI/air/station/?lang=en

def AQD_reader(csv_file):
    csv_file_name = os.path.basename(csv_file)
    csv_file_date = csv_file_name[:4]

    df = pd.read_csv(csv_file, skiprows=5)
    df.columns = df.columns = ['Year', 'Pollutant', 'Station', 'Month 01', 'Month 02', 'Month 03', 'Month 04', 'Month 05', 'Month 06', 'Month 07', 'Month 08', 'Month 09', 'Month 10', 'Month 11', 'Month 12']
    df = df.replace('N.A.', pd.NA)
    # Remove the time component from the Date column
    
    df.to_excel(f'csv_to_excel/air_data.xlsx', index=False)
    print('Excel file generated')

AQD_reader('Raw_data/2018-2022_air_monthly.csv')