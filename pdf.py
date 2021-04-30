import openpyxl
import fpdf

pdf = fpdf.FPDF()
pdf.add_page()
pdf.add_font("PT Serif", "", "d:/SOFT/freefonts/all_fonts/PTF55F.ttf", uni=True)
pdf.add_font("NotoSerif-Regular", "", "d:/SOFT/freefonts/all_fonts/NotoSerif-Regular.ttf", uni=True)
pdf.add_font("Exo2", "", "d:/SOFT/freefonts/all_fonts/Exo2-Regular.ttf", uni=True)

pdf.set_font("Exo2", '', 16)

udo_path = "c:/Users/typo/Documents/!!ГОС_ДИП_УД/УДОСТОВЕРЕНИЯ_ДАННЫЕ/удостоверения.xlsx"
wb = openpyxl.load_workbook(filename = udo_path)
ws = wb.active
pdf.cell(40, 10, ws["m3458"].value)
pdf.output('удостоверения.pdf', 'F')