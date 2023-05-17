mydict={'id':1,'name':'sanket','sub':'python'}
"""print(mydict)
print(mydict['sub'])
print(mydict.get('id'))

print(len(mydict))"""

print(mydict)
print(mydict.keys())
print(mydict.values())

"""if 'name' in mydict:
    print("Yes...")
else:
    print("Noo")"""

"""if 'sanket' in mydict.values():
    print("Yes...")
else:
    print("Noo")"""

"""for i in mydict:
    print(i)"""

"""for i in mydict.values():
    print(i)"""

for i in mydict.items():
    print(i)