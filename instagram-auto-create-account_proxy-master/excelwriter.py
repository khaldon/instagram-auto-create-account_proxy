######### This is my original code ################
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import DataFrame
from openpyxl import Workbook




df1 = pd.DataFrame([50,"desfdf","desfdf",55])
df2 = pd.DataFrame([50,"desfdf","desfdf",55])

var = len(df1.iloc[:,0:])
print(var)
x1 = 'mypath/ '
x2 = 'test'
x3 = '.xlsx'
destination = x2  + x3
writer = pd.ExcelWriter(destination, engine='xlsxwriter')

df1.to_excel(writer, sheet_name= 'Returns 1',startcol=0,startrow=var )
df2.to_excel(writer, sheet_name= 'Returns 2')
writer.save()