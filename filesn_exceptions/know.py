import json

try:
    with open(r"filesn_exceptions\numbers.json") as file:
        data = json.load(file)
except:
    info = {"name":input("What is your name?"),
    "age":input("How old are you?")}
    with open(r"filesn_exceptions\numbers.json",'w') as file:
        json.dump(info,file)
else:
    print(f"Welcome back {data['name']}, i remember you're {data['age']} right?")

    


    