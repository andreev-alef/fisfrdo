import openpyxl

wb = openpyxl.load_workbook(filename="openpyxl-удостоверения.xlsx", data_only=True)
ws = wb.active
print(ws["e3456"].value)
print(ws["f3456"].value)
print(ws["g3456"].value)
print(ws["i3456"].value)
print(ws["j3456"].value)
print(ws["k3456"].value)
print(ws["L3456"].value)
print(ws["M3456"].value)
print(ws["n3456"].value)