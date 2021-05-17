import pdfkit
#    <meta charset="utf-8" />
html_str = '''
<!DOCTYPE html>
<html lang="ru">
<head>

</head>
<body>
    <p><span style="color: #000000; font-family: Exo2; font-size: 16pt;"><b>Проба пера</b>. Синий</span></p>
    <p><span style="color: #ff0000; font-family: 'Noto Serif'; font-size: 16pt;"><b>Проба пера №2</b></span><br />
    Разрыв строки
    </p>

</body>
</html>
'''

ops = {
    'page-size': 'Letter',
    'margin-top': '10mm',
    'margin-right': '10mm',
    'margin-bottom': '10mm',
    'margin-left': '10mm',
    'encoding': "UTF-8",
    'orientation':'Landscape'}
pdfkit.from_string(html_str, 'data.pdf', options=ops)
