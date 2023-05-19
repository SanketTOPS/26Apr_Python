mydict={'id':1,'name':'sanket','sub':'python'}
"""print(mydict)
print(mydict['sub'])
print(mydict.get('id'))

print(len(mydict))"""

#print(mydict)
#print(mydict.keys())
#print(mydict.values())

"""if 'sub' in mydict:
    print("Yes...")
else:
    print("Noo")"""

"""if 'python' in mydict.values():
    print("Yes...")
else:
    print("Noo")"""

"""for i in mydict:
    print(i)"""

"""for i in mydict.values():
    print(i)"""

"""for i in mydict.items():
    print(i)"""

#Key=id and Value=1
#Key=name and Value=sanket

"""for i,j in mydict.items():
    #print(i,j)
    print(f"Key={i} and Value={j}")"""

"""print(mydict)
mydict['id']=2
mydict['name']='ashok'"""
#print(mydict)
#mydict['city']='rajkot'
#mydict.pop('sub')
#del mydict['city']
#mydict.clear()
print(mydict)

newdict=mydict.copy()
print(newdict)