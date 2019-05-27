#!/usr/local/bin/python3.7
# index.py 5/27/2019 dwg - 
# Copyright (C) 2019 Douglas Wade Goodall. All Rights Reserved.

import cgi
import datetime
import os

print("Content-type:\ttext/html\n\n")

##################################################################################
## This code displays a table showing the bill of materials for this script.    ##
## the bill of materials only displays if there is a "bom" parameter in the URL ##
##################################################################################
form = cgi.FieldStorage()
try:
    bBOM = str(form["bom"].value)
    print("<table columns=1 border=1><tr><th>Bill of materials: Module"
          "</th><th>Last modification date/time</th></tr>")
except:
    pass    
from langbind import *
import globbind
import htmlbind
try:
    bBOM = str(form["bom"].value)
    print("<tr><td>"+os.getcwd()+"/"+__file__+"</td><td>"
          +str(datetime.datetime.fromtimestamp(os.path.getmtime(__file__)))+"</td></tr>")
    print("</table>")
except:
    pass
#########################################################################################

fd = open("_index.html","w")
fd.write("<center>")
fd.write("<img src=\""+LB_logo+"\">")
fd.write("</center>")
fd.close()

fd = open("_index.html","r")
data = fd.read()
fd.close()
print(data)
