#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import cgi
print("""Content-Type: application/json\n""")
form = cgi.FieldStorage() 
a=form.getlist('data')[0]
a=int(a)+1
x={"value":a}
y = json.dumps(x)
print(y)
