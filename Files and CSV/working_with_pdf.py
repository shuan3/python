import tabula

# pip install tabula-py
# pyPDF2
import pandas as pd

# Read pdf into list of DataFrame
# dfs = tabula.read_pdf("test.pdf", pages='all')
from tabula.io import read_pdf

# Read remote pdf into list of DataFrame

# tabula.convert_into(r"C:\Users\shanh\Downloads\Visa Statement-0849 2023-08-21.pdf", "output.csv", output_format="csv", pages='all')

df = tabula.io.read_pdf(
    r"C:\Users\shanh\Downloads\Visa Statement-0849 2023-08-21.pdf",
    stream=True,
    pages="all",
)
print(len(df))
# print(df)
# df=pd.DataFrame(df)
# df.to_csv('output.csv',index=False)
# tabula.convert_into(r"C:\Users\shanh\Downloads\Visa Statement-0849 2023-08-21.pdf", "output.csv", output_format="csv", pages='all')
dff = pd.concat(pd.DataFrame(fl) for fl in df)
dff.to_csv("output.csv", index=False)

# for i in df:
#     i.to_csv("output.csv", index = False)

# from PyPDF2 import PdfReader

# reader = PdfReader(r"C:\Users\shanh\Downloads\Visa Statement-0849 2023-08-21.pdf")
# number_of_pages = len(reader.pages)
# print(reader.cache_indirect_object )
