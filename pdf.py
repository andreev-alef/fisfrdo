import openpyxl
import fpdf

udo_path = "c:/Users/typo/Documents/!!ГОС_ДИП_УД/УДОСТОВЕРЕНИЯ_ДАННЫЕ/удостоверения.xlsx"
wb = openpyxl.load_workbook(filename = udo_path)
ws = wb.active

html = """
<H1 align="center"></H1>
<h2>Basic usage</h2>
<p>You can now easily print text mixing different
styles : <B>bold</B>, <I>italic</I>, <U>underlined</U>, or
<B><I><U>all at once</U></I></B>!<BR>You can also insert links
on text, such as <A HREF="http://www.fpdf.org">www.fpdf.org</A>,
or on an image: click on the logo.<br>
<center>
<A HREF="http://www.fpdf.org"><img src="logo.jpg" width="20mm"></A>
</center>
<h3>Sample List</h3>
<ul><li>option 1</li>
<ol><li>option 2</li></ol>
<li>option 3</li></ul>

<table border="0" align="center" width="50%">
<thead><tr><th width="30%">Header 1</th><th width="70%">header 2</th></tr></thead>
<tbody>
<tr><td>cell 1</td><td>cell 2</td></tr>
<tr><td>cell 2</td><td>cell 3</td></tr>
</tbody>
</table>
"""

class MyFPDF(fpdf.FPDF, fpdf.HTMLMixin):
    pass
pdf = MyFPDF()
pdf.add_page()
pdf.add_font("PT Serif", "", "d:/SOFT/freefonts/all_fonts/PTF55F.ttf", uni=True)
pdf.add_font("NotoSerif-Regular", "", "d:/SOFT/freefonts/all_fonts/NotoSerif-Regular.ttf", uni=True)
pdf.add_font("Exo2", "", "d:/SOFT/freefonts/all_fonts/Exo2-Regular.ttf", uni=True)
pdf.set_font("Exo2", '', 16)
pdf.write_html(html)
pdf.output('удостоверения.pdf', 'F')