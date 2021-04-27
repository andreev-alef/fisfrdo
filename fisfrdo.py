import openpyxl

wb = openpyxl.load_workbook(filename="openpyxl-удостоверения.xlsx", data_only=True)
ws = wb.active
print(ws["e3456"].value,
      ws["f3456"].value,
      ws["g3456"].value,
      ws["i3456"].value,
      ws["j3456"].value,
      ws["k3456"].value,
      ws["L3456"].value,
      ws["M3456"].value,
      ws["n3456"].value)