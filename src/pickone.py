import json
import os
from collections import OrderedDict
from utils import codelist, loadJsonFile

def pickone(nlsjson, sKey, tKey):
    sKeyList = sKey.split(">")
    tKeyList = tKey.split(">")
    sValue = getSValue(nlsjson,sKeyList)
    setTValue(nlsjson, tKeyList, sValue)
            
        
def getSValue(nlsjson, sKeyList):
    for sk in sKeyList:
        if isinstance(nlsjson[sk], dict):
            nlsjson = nlsjson[sk]
        else:
            return nlsjson[sk]

def setTValue(nlsjson, tKeyList, value):
    for tk in tKeyList:
        if tk in nlsjson and isinstance(nlsjson[tk],dict):
            nlsjson = nlsjson[tk]
        else:
            nlsjson[tk] = value

def main():
    dirName = input("NLS directory:")
    sourceKey = input("source key:")
    targetkey = input("target key:")
    dir = os.listdir(dirName)
    for fileName in dir:
        if fileName.replace(".json","") in codelist:
            j = loadJsonFile(dirName+"//"+fileName)
            pickone(j,sourceKey,targetkey)
            save = open(dirName+"//"+fileName, "w", encoding="UTF-8")
            save.write(json.dumps(j, indent=4, ensure_ascii=False))