import openpyxl
import re

udo_path = "c:/Users/typo/Documents/!!ГОС_ДИП_УД/УДОСТОВЕРЕНИЯ_ДАННЫЕ/удостоверения.xlsx"
frdo_shablon = "c:/Users/typo/Documents/!!ГОС_ДИП_УД/!!!ФИСФРДО/Шаблон_апрель_2021.xlsx"
wb_udo = openpyxl.load_workbook(filename = udo_path, data_only=True)
ws_udo = wb_udo.active
wb_frdo = openpyxl.load_workbook(filename = frdo_shablon, data_only=True)
ws_frdo = wb_frdo.active

i = 0
r = ws_udo["A3499":"N3500"]
# print("{0}    {1}    {2}    {3}    {4}    {5}    {6}    {7}".format(r[1][5].value,
#                                                       r[1][6].value,
#                                                       r[1][8].value,
#                                                       r[1][9].value,
#                                                       r[1][10].value,
#                                                       r[1][11].value,
#                                                       r[1][12].value,
#                                                       r[1][13].value))
period = r[i][11].value
volume = r[i][13].value
#otch = r[1][10].value
otch = "Викторовна"

print(re.findall("[0-9]{4}", period))
print(re.findall("[0-9]{1,3}", volume))
if re.search(".*вич", otch):
    print("муж")
else:
    print("жен")

