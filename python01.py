import pandas as pd

# Assign spreadsheet filename to `file`
file = 'example.xlsx'

# Load spreadsheet
excel = pd.read_excel(file)

ages = excel["Age"]
print(ages.head())


#print(df1)
# Load a sheet into a DataFrame by name: df1
# df1 = xl.parse('Sheet1')

#writer = pd.write_excel('new-example.xlsx', engine='xlsxwriter')


# df1 = pd.DataFrame(ages.head(),
#                    columns=['col 1', "Ages"])

ages.to_excel("resultats.xlsx")