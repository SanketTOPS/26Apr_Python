import re

mystr="This is Python!8956"

#x=re.findall('^This',mystr)
#x=re.findall('^[A-Z]',mystr)
#x=re.findall('[^A-Z]',mystr)
x=re.findall('56$',mystr)
print(x)
