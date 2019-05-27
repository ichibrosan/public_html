#!/usr/local/bin/python3.7
# globbind.py 5/27/2019 dwg - initial version
import cgi
import datetime
import os
form = cgi.FieldStorage()
try:
    bBOM = str(form["bom"].value)
    print("<tr><td>"+__file__+"</td><td>"+str(datetime.datetime.fromtimestamp(os.path.getmtime(__file__)))+"</td></tr>")
except:
    pass


RMJ = 1
RMN = 0
RUP = 0
RTP = 0
