import openpyxl
import re
import tornado.web
import pdfkit
import mysql.connector

udo_path = "c:/Users/typo/Documents/!!ГОС_ДИП_УД/УДОСТОВЕРЕНИЯ_ДАННЫЕ/удостоверения.xlsx"
frdo_shablon = "c:/Users/typo/Documents/!!ГОС_ДИП_УД/!!!ФИСФРДО/Шаблон_апрель_2021.xlsx"
wb_udo = openpyxl.load_workbook(filename = udo_path, data_only=True)
ws_udo = wb_udo.active
wb_frdo = openpyxl.load_workbook(filename = frdo_shablon, data_only=True)
ws_frdo = wb_frdo.active

i = 2
r = ws_udo["A3498":"N3506"]
if r[i][5].value is not None:
    print(r[i][5].value is not None)
    user = {"gosnomer":r[i][5].value,
            "reg_nomer":r[i][6].value,
            "fam":r[i][8].value,
            "im":r[i][9].value,
            "ot":r[i][10].value,
            "period":r[i][11].value,
            "tema":r[i][12].value,
            "objem":r[i][13].value}
    print("{0}    {1}    {2}    {3}    {4}    {5}    {6}    {7}".format(user["gosnomer"],
                                                          r[i][6].value,
                                                          r[i][8].value,
                                                          r[i][9].value,
                                                          r[i][10].value,
                                                          r[i][11].value,
                                                          r[i][12].value,
                                                          r[i][13].value))
    period = r[i][11].value
    volume = r[i][13].value
    #otch = r[i][10].value
    otch = "Викторовна"

    per = re.findall("[0-9]{4}", period)
    for p in per:
        print(p)
    vol = re.findall("[0-9]{2,}", volume)
    for v in vol:
        print(v)
    if re.search(".*вич", otch):
        print("муж")
    else:
        print("жен")

else:
    print("Пустая строка")