from random import randint
import json

# Generating data
data = ""
data_json = []
for k in range(1,50034):
    num = randint(1,999999999)
    data_json.append(num)
    data += f"{str(num)}\n"
    
with open(r"C:\Users\Windows\Desktop\Stuff\Coding\PY\filesn_exceptions\data.txt") as file:
    # Getting all the lines
    # content = file.read()
    total = 0
    # Line by line
    for line in file:
        total += int(line)
    print(total)

with open(r"C:\Users\Windows\Desktop\Stuff\Coding\PY\filesn_exceptions\data.txt",'w') as fileobj:
    fileobj.write(data)

with open(r"filesn_exceptions\numbers.json","w") as jsonFile:
    json.dump(data_json,jsonFile)
    
    
with open(r"filesn_exceptions\numbers.json") as jsonFile:
    numbers = json.load(jsonFile)
    print(type(numbers))