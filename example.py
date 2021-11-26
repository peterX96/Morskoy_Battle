import json

with open('example.json') as json_file:
    x = json.load(json_file)

print(type(x))
print(x)
print(x["firstName"])
print(x["lastName"])
