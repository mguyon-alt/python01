import pandas as pd

# Assign spreadsheet filename to `file`
file = 'Agro.xlsx'

# Load spreadsheet
excel = pd.read_excel(file)

nbAjout=0
data = []

for index, row in excel.iterrows():
    id=row[0]
    nomLab=row[1]
    cp= row[4]
    if isinstance(cp, int) and ((cp > 75000) and (cp < 76000)) :
        data.append(row)
        nbAjout+=1
    if isinstance(cp, int) and ((cp > 78000) and (cp < 79000)) :
        data.append(row)
        nbAjout+=1
    if isinstance(cp, int) and ((cp > 92000) and (cp < 93000)) :
        data.append(row)
        nbAjout+=1
    if isinstance(cp, int) and ((cp > 94999) and (cp < 96000)) :
        data.append(row)
        nbAjout+=1

print("Ajouts : "+ str(nbAjout))

#creation du dataframe pour le nouveau tableau avec nouvelles donnees
newExcel = pd.DataFrame(data)
del newExcel[0]

# Creation du fichier excel
newExcel.to_excel("resultats.xlsx")
