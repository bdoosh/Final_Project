# write to a json file
import json

def createJSON(layout):

    with open("pagecontent.json", "w", encoding="utf=8") as output_file:
       json.dump(layout, output_file, indent=4)