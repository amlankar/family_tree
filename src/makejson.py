import json
import csv

def dictmake(key):
    dict_in = {}
    dict_in["name"] = key
    if key in sg:
	sg.remove(key)
	dict_in["children"] = []
	for child in sgdict[key]:
	    dict_in["children"].append(dictmake(child))
    
    return dict_in


sgdict = {}
##Make a dictionary with key as SG and value as an array of his/her bacchas/bacchis from csv file

with open("../resources/sg.csv","rb") as sgfile:
    reader = csv.reader(sgfile)
    for row in reader:
	key = row[0].lower().title().strip()+"-"+row[1]
	value = row[2].lower().title().strip()+"-"+row[3]
	if key not in sgdict.keys():
	    sgdict[key] = []
	sgdict[key].append(value)

sg = []
sg = sgdict.keys() ##Will use this array to control the recursive function

jsondict = {}
jsondict["name"] = "all"
jsondict["children"] = []

with open("../resources/sg.csv","rb") as sgfile:
    reader = csv.reader(sgfile)
    for row in reader:
	key = row[0].lower().title().strip()+"-"+row[1]
	if key in sg:
	    jsondict["children"].append(dictmake(key))

with open("js/data.json","wb") as file:
    json.dump(jsondict,file)

