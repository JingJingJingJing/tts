import json
import os
from collections import OrderedDict
import re
   
def synca(node, target):
    for key in node:
        if isinstance(node[key],dict):
            if key in target:
                synca(node[key],target[key])
        else:
            if "<a" in node[key] and key in target:
                olds = geta(node[key])
                news = geta(target[key])
                if len(olds) == len(news):
                    for i,old in enumerate(olds):
                        node[key] = node[key].replace(old,news[i],1)

def geta(s):
    pattern = re.compile("(<a.*?>).*?</a>")
    return re.findall(pattern,s)


sl = {"ar","cs","da","de","el","en","es","fi","fr","he","hr","hu","it","ja","ko","nb","nl","pl","pt","pt-BR","ro","ru","sk","sl","sr-Latn","sv","tr","uk","zh-hans","zh-hant"}
dirName = input("NLS directory:")
dir = os.listdir(dirName)
target = json.load(open(dirName+"//target.json"),object_pairs_hook=OrderedDict)
for fileName in dir:
    if fileName.replace(".json","") in sl:
        tbc = open(dirName+"/"+fileName, "r")
        tbcj = json.load(tbc, object_pairs_hook=OrderedDict)
        synca(tbcj,target)
        tbc = open(dirName+"//"+fileName, "w")
        tbc.write(json.dumps(tbcj, indent=4))
        
