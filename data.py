from flask import json

exemplo = {
    "title":"Nota 1",
    "description":"lalala",
    "date":"Sep, 28th 2021",
    "id":0
}

json_object = json.dumps(exemplo, indent = 4)

with open('data_files.json', 'w') as outfile:
    outfile.write(json_object)