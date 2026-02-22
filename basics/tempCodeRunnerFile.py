import os
import openpyxl

os.chdir(r"C:\Users\safab\OneDrive\Desktop")

workbook = openpyxl.load_workbook("secret.xlsx")
sheet1 = workbook["Sheet1"] # Go to sheet 1
print(sheet1["A2"].value) # Go to the cell A1 and for .value to gives as just the valur of the cell