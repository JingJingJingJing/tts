import os
import json
from collections import OrderedDict
from utils import codelist, loadJsonFile

def append(tbc, adt, std):
    for key in adt:
        if isinstance(adt[key],dict):
            if key in tbc and key in std:
                append(tbc[key],adt[key],std[key])
            elif key not in tbc and key in std:
                insert(tbc,adt,std,key)
        else:
            if key in tbc:
                tbc[key] = adt[key]
            else:
                insert(tbc,adt,std,key)

def insert(node, add, std, key):
    after = False
    for k in std:
        if not after and k == key:
            after = True
            node[key] = add[key]
        if after and k in node:
            node.move_to_end(k)    
                        
def main():
    dirName = input("NLS directory:")
    appendDir = input("append directory:")
    dir = os.listdir(dirName)
    target = json.load(open(dirName+"//en.json", encoding="UTF-8"), object_pairs_hook=OrderedDict)
    for fileName in dir:
        if fileName.replace(".json","") in codelist:
            adtj = loadJsonFile(appendDir+"//"+fileName)
            tbcj = loadJsonFile(dirName+"//"+fileName)
            append(tbcj,adtj,target)
            tbc = open(dirName+"//"+fileName, "w", encoding="UTF-8")
            tbc.write(json.dumps(tbcj, indent=4, ensure_ascii=False))
