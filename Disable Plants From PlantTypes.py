import json

exceptions = {} # put your exceptions here!!

with open("PLANTTYPES.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for obj in data["objects"]:
    objdata = obj.get("objdata", {})
    name = objdata.get("TypeName")

    if name not in exceptions:
        if "Enabled" not in objdata:
            objdata["Enabled"] = False

with open("PLANTTYPES_Modded.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

input("Ready!! enjoy you modder!!")