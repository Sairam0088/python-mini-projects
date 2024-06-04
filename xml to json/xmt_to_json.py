# Xml to json converter
import json
import xmltodict

with open(r"xml to json\input.xml") as xml_file:
    xml_parsed_data = xmltodict.parse(xml_file.read())
    xml_file.close()
    
    json_data = json.dumps(xml_parsed_data)
    
with open("xml to json\\output.json", "w") as json_file:
    json_file.write(json_data)
    json_file.close()
    print("Converted Successfully")