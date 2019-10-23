import os

fPath = 'C:\\Users\\Tyler\\Desktop\\The-Tech-Academy-Python-Coding-Projects\\SourceDir'

for file in os.listdir(fPath):
    if file.endswith(".txt"):
        abPath = os.path.join(fPath, file)
        print(file)
        print(">> {}".format(os.path.getmtime(abPath)))


           





