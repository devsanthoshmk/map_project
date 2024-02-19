import re

a="sdfllsj dlkfjsljfas dflkjasfjas fasdflkjasdf aspf aspfjasfjsd flsjf faspjfajfu040390 A00JD 08R0W8084080 808080 ;';'..';'.."
b=re.findall("[a-zA-Z0-9]|[' ']",a)
print(b)