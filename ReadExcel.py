import pandas as pd
from pandas import *

excel_file = 'E://Python Workspace//pythonReadExcel.xlsx'
movies = pd.read_excel(excel_file)

print(movies.head(1))

df = pd.DataFrame(movies)
rows = len(df.axes[0])
cols = len(df.axes[1])

print("Number of Rows: "+str(rows))
print("Number of Columns: "+str(cols))

# DF returns the whole excel
# print(df)

###########################################################################################################
# get excel value in dictionary
# xls = ExcelFile('E://Python Workspace//pythonReadExcel.xlsx')
# dfs = xls.parse(xls.sheet_names[0])
# print(dfs.to_dict())
##  {'name': {0: 'Candy', 1: 'Robot'}, 'roll': {0: 1, 1: 2}, 'office': {0: 'CTS', 1: 'CTS'}}
###########################################################################################################
# Another WAY
###########################################################################################################
# # reading csv file from url
# data = pd.read_excel('E://Python Workspace//pythonReadExcel.xlsx')
# # dropping null value columns to avoid errors
# data.dropna(inplace=True)
# # converting to dict
# data_dict = data.to_dict()
# # display
# print(data_dict)
## {'name': {0: 'Candy', 1: 'Robot'}, 'roll': {0: 1, 1: 2}, 'office': {0: 'CTS', 1: 'CTS'}}
###########################################################################################################
