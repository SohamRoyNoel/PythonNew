import pandas as pd
from xlrd import *
df = pd.read_excel('E://Python Workspace//pythonReadExcel.xlsx', nrows=1)

# {'name': {0: 'Candy'}, 'roll': {0: 1}, 'office': {0: 'CTS'}}
dict = df.to_dict()

sub_dict = dict["name"]  # {0: 'Candy'}

print(sub_dict[0])  # Candy

df = pd.DataFrame(pd.read_excel('E://Python Workspace//pythonReadExcel.xlsx'))
print(df)

for i in df.index:
    print(df['name'][i])

# Candy
# Robot
###################################################################################################
dfs = pd.read_excel('E://Python Workspace//pythonReadExcel.xlsx',  skiprows=0)
recArr = dfs.to_dict(orient='records')
# [{'name': 'Candy', 'roll': 1, 'office': 'CTS'}, {'name': 'Robot', 'roll': 2, 'office': 'CTS'}]
###################################################################################################
noofElementsInList = len(recArr)  # 2

res = recArr[0]
print(res)   # {'name': 'Candy', 'roll': 1, 'office': 'CTS'}
print(res['office'])   # CTS
###################################################################################################
counter = 0
toBeIterate = noofElementsInList-1

while toBeIterate >= counter:
    getmap = recArr[counter]
    name = getmap['name']
    roll = getmap['roll']
    office = getmap['office']
    print(name, roll, office)
    counter += 1
# Candy 1 CTS
# Robot 2 CTS
