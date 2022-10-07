import json

f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

newData = []

print(type(data))

for i in data:
    #print(i)
    newDict = i
    newDict.pop("_rid", None)
    newDict.pop("_self", None)
    newDict.pop("_etag", None)
    newDict.pop("_ts", None)
    newDict.pop("_attachments", None)

    print(newDict)
    newData.append(newDict)

json_object = json.dumps(newData, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)


# Closing file
f.close()