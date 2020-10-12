#Code to convert an excel workbook that contains multiple sheets to csv format

import pandas as pd

path=input("Input the location of excel file: ")
excel_file = path

all_sheets = pd.read_excel(excel_file, sheet_name=None)
sheets = all_sheets.keys()

dest = input("Input the location for csv files")
dest = dest + "/%s.csv"

for sheet_name in sheets:
    sheet = pd.read_excel(excel_file, sheet_name=sheet_name)
    sheet.to_csv(dest % sheet_name, index=False)
