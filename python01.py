import pandas as pd

# Assign spreadsheet filename to `file`
file = '/Users/guyon/Documents/Codes/example.xlsx'

# Load spreadsheet
xl = pd.read_excel(file)

# Print the sheet names
print(xl)

# Load a sheet into a DataFrame by name: df1
# df1 = xl.parse('Sheet1')