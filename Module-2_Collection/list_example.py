data=['python','java','android','c++','php']
#print(data)

"""print(data[0])
print(data[-1])
print(data[0:3])
print(data[2:])
print(data[:3])
"""
#print(data[:-1])

#print(data)
#data[2]='iOS'
#print(data)

"""for i in data:
    print(i)"""


#print(data.index('java'))

"""for i in data:
    #print(i)
    print(f"{data.index(i)}={i}")"""

"""n=0
for i in data:
    print(f"{n}={i}")
    n+=1"""

"""if 'PHP' in data:
    print("Yes...")
else:
    print("Noo")"""


#print(len(data))

#------------------------------------------------------------------#

print(data)
#data.append('angular')
#data.insert(2,'react')
#data.remove('php')
#data.pop()
#data.pop(1)
#data.clear()
#del data[2]
#del data
#data.sort()
#data.reverse()
#print(data)

#newlist=data.copy()
newlist=['C',"HTML","CSS","JS"]
print(newlist)

#print(data+newlist)
data.extend(newlist)
print(data)