import openpyxl
udo_path = "c:/Users/typo/Documents/!!ГОС_ДИП_УД/УДОСТОВЕРЕНИЯ_ДАННЫЕ/удостоверения.xlsx"
frdo_shablon = "c:/Users/typo/Documents/!!ГОС_ДИП_УД/!!!ФИСФРДО/Шаблон_апрель_2021.xlsx"
wb_udo = openpyxl.load_workbook(filename = udo_path, data_only=True)
ws_udo = wb_udo.active
wb_frdo = openpyxl.load_workbook(filename = frdo_shablon, data_only=True)
ws_frdo = wb_frdo.active

r = ws_udo["D3485":"H3490"]
for i in r:
    for j in i:
        print(j.value)