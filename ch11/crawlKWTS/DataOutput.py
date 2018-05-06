# -*- coding: utf-8 -*-
import codecs
import time


class DataOutput(object):

    def __init__(self):
        self.filepath = 'kuwo.html'
        self.output_head(self.filepath)

    def output_head(self, path):
        fout = codecs.open(path, 'w', encoding="utf-8")
        fout.write("<html>")
        fout.write("<head>")
        fout.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")

        fout.close()
        return


    def output_html(self, path, datas):
        if datas == None:
            return

        fout = codecs.open(path, 'a', encoding="utf-8")

        for data in datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['file_id'])
            fout.write("<td>%s</td>" % data['name'])
            fout.write("<td>%s</td>" % data['file_path'])
            fout.write("</tr>")
        fout.close()
        return


    def output_end(self, path):
        fout = codecs.open(path, 'a', encoding="utf-8")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()
        return