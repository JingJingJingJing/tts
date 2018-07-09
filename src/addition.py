import os
import json
from collections import OrderedDict

def append(tbc, adt, std):
    for key in adt:
        if isinstance(adt[key],dict):
            if key in tbc and key in std:
                append(tbc[key],adt[key],std[key])
        else:
            if key in tbc:
                tbc[key] = adt[key]
            else:
                for k in std:
                    after = False
                    if not after and k == key:
                        after = True
                        tbc[key] = adt[key]
                    if after:
                        tbc.move_to_end(k)
                        
                    

sl = {"ar","cs","da","de","el","en","es","fi","fr","he","hr","hu","it","ja","ko","nb","nl","pl","pt","pt-BR","ro","ru","sk","sl","sr-Latn","sv","tr","uk","zh-hans","zh-hant"}
dirName = input("NLS directory:")
appendDir = input("append directory:")
dir = os.listdir(dirName)
target = json.load(open(dirName+"//target.json"),object_pairs_hook=OrderedDict)
for fileName in dir:
    if fileName.replace(".json","") in sl:
        tbc = open(dirName+"//"+fileName, "r")
        adtj = json.load(open(appendDir+"//"+fileName, "r"), object_pairs_hook=OrderedDict)
        tbcj = json.load(tbc, object_pairs_hook=OrderedDict)
        append(tbcj,adtj,target)
        tbc = open(dirName+"//"+fileName, "w")
        tbc.write(json.dumps(tbcj, indent=4))
