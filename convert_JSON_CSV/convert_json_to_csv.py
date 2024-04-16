import json

with open(r"convert_JSON_CSV\input.json", "r") as jsonfile:
    data = json.loads(jsonfile.read())

output = ",".join([*data[0]])

for person in data:
    output += f"\n{person["Name"]},{person["age"]},{person["place"]}"

with open("convert_JSON_CSV\\output.csv", "w") as csvfile:
    csvfile.write(output)
    print("Successfully converted")