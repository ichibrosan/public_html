#!/usr/local/bin/python3.7
# htmlbind.py 5/27/2019 dwg - initial version
import cgi
import datetime
import os
form = cgi.FieldStorage()
try:
    bBOM = str(form["bom"].value)
    print("<tr><td>"+__file__+"</td><td>"+str(datetime.datetime.fromtimestamp(os.path.getmtime(__file__)))+"</td></tr>")
except:
    pass


