import os

#os.mkdir("Myfolder")

"""os.chdir('Myfolder/Subfolder')
os.mkdir('Newfolder')"""

"""os.chdir('Newfolder')
open('myfile.txt','x')"""

"""os.chdir('Myfolder/Subfolder/Newfolder')
open('hello.xls','x')"""

"""if os.path.exists('Testfolder'): #true
    print("Error!Folder is already created")
else:
    os.mkdir('Testfolder')
    print("folder is created!")"""

# File remove
#os.remove('test.txt')


# Folder remove
#os.removedirs('Testfolder')

os.removedirs('Newfolder')

"""os.chdir('Newfolder')
os.remove('myfile.txt')"""
