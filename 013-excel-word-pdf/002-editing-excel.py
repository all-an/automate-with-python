import openpyxl, os

wb = openpyxl.Workbook()

print(type(wb))

print(wb.sheetnames)

sheet1 = wb['Sheet']

print(type(sheet1))

print(sheet1['A1'].value == None)

sheet1['A1'] = 42
sheet1['A2'] = 'Hello'