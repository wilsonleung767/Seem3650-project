import pandas as pd

# read data from Excel file
df = pd.read_excel('data/tunnelCarFlow2018-2022.xls',  header=None, skiprows=17, nrows=, usecols="C:P")

# assign values to row 24 of DataFrame
# row_index = 23  # zero-based index of row 24
# df.iloc[row_index] = df.values

# print DataFrame to verify results
print(df)