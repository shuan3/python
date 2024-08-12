# pandas
# openpyxl  specialized for excel
# google sheets python api
import pandas as pd

import csv

# data=open('Files and CSV\example.csv',encoding='utf-8')

# csv_data=csv.reader(data)
# data_lins=list(csv_data)
# D:\Github\test\Files and CSV\example.csv
data = pd.read_csv(r"D:\Github\test\Files and CSV\example.csv", encoding="utf-8")
print(data.head(5))
