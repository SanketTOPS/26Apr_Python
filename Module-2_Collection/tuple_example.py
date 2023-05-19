data=('rajkot','surat','ahmedabad','baroda','jamnagar')
"""print(data)
print(data[0])
print(data[-1])
print(data[0:3])
print(data[:3])
print(data[2:])"""

#print(len(data))

"""if 'surat' in data:
    print("Yes..")
else:
    print("Noo")"""

print(data)
print(data.index('surat'))

for i in data:
    #print(i)
    print(f"{data.index(i)}={i}")

del data
print(data)