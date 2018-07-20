import os
import json
from collections import OrderedDict

def compare_switch(new, old):
    for key in new:
        if key not in old:
            return
        if isinstance(new[key],dict):
            if isinstance(new[key],dict):
                compare_switch(new[key], old[key])
            else:
                old[key] = new[key]
        else:
            if new[key] != old[key]:
                old[key] = new[key]

sl = {"ar","cs","da","de","el","en","es","fi","fr","he","hr","hu","it","ja","ko","nb","nl","pl","pt","pt-BR","ro","ru","sk","sl","sr-Latn","sv","tr","uk","zh-hans","zh-hant"}
nls_dir = os.listdir(input("NLS directory:"))
return_dir = os.listdir(input("return directory:"))
for fileName in nls_dir:
    lang = fileName.replace(".json","")
    if lang in sl and lang in return_dir:
        oldj = json.load(open(nls_dir+"//"+fileName, "r"), object_pairs_hook=OrderedDict)
        newj = json.load(open(return_dir+"//"+fileName, "r"), object_pairs_hook=OrderedDict)
        compare_switch(oldj, newj)
        old = open(nls_dir+"//"+fileName, "w")
        old.write(json.dumps(oldj, indent=4))