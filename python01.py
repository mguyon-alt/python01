import pandas as pd

# Assign spreadsheet filename to `file`
file = 'Agro.xlsx'

# Load spreadsheet
excel = pd.read_excel(file)

# cp = excel["4"]
# print(cp.head())


#print(df1)
# Load a sheet into a DataFrame by name: df1
# df1 = xl.parse('Sheet1')

#writer = pd.write_excel('new-example.xlsx', engine='xlsxwriter')


# df1 = pd.DataFrame(ages.head(),
#                    columns=['col 1', "Ages"])
newExcel= pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
nbAjout=0
data = []
for index, row in excel.iterrows():
    #colonne=newExcel.iloc[[0]]
    id=row[0]
    nomLab=row[1]
    cp= row[4]
    if isinstance(cp, int) and (cp > 75000) :
        data.append(row)
        nbAjout+=1

print("Ajouts : "+ str(nbAjout))
newExcel = pd.DataFrame(data)
newExcel.to_excel("resultats.xlsx")
