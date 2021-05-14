import pdfkit

html_str = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8" />
</head>
<body>
    <p><span style="color: #000000; font-family: Exo2; font-size: 16pt;"><b>Проба пера</b>. Синий</span></p>
    <p><span style="color: #ff0000; font-family: 'Noto Serif'; font-size: 16pt;"><b>Проба пера №2</b></span><br />
    Разрыв строки
    </p>
</body>
</html>
'''
pdfkit.from_string(html_str, 'data.pdf')