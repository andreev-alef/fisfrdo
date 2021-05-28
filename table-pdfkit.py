import pdfkit

s = '''
<html>
<head>
    <meta charset="utf-8" />
    <style>
        body{
            margin: 30mm;
        }
        table{
            border: solid #fff 0.25mm;
            padding: 0;
            border-spacing: 0px;
            border-collapse: collapse;
            width: 100%
        }
        th{
            border: solid #000 0.25mm;
            padding: 2mm;
        }
        td{
            border: solid #000 0.25mm;
            padding: 2mm;
        }
    </style>
</head>
    <body>
    <table>
        <th>
            Первая ячейка заголовок
        </th>
        <th>
            Вторая ячейка  заголовок
        </th>
        
        <tr>
            <td>Первая ячейка
            <td>Вторая ячейка
        </tr>
        <tr>
            <td>строка 2</td>
            <td>лыоавыдаоывфаждлвоыа</td>
        </tr>
    </table>
    </body>
</html>
'''
pdfkit.from_string(s, 'out.pdf')