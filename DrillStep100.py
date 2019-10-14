import os

fPath = 'C:\\DrillStep100Dir\\'

for file in os.listdir(fPath):
    if file.endswith(".txt"):
        abPath = os.path.join(fPath, file)
        print(file)
        print(">> {}".format(os.path.getmtime(abPath)))


           





