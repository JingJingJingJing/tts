import os
import json
from collections import OrderedDict
from constant import codelist

def compare_switch(new, old):
    for key in new:
        if key not in old:
            return
        if isinstance(new[key],dict):
            compare_switch(new[key], old[key])
        else:
            if new[key] != old[key]:
                old[key] = new[key]

def main():
    nls_dir = input("NLS directory:")
    return_dir = input("return directory:")
    for fileName in os.listdir(nls_dir):
        lang = fileName.replace(".json","")
        if lang in codelist and fileName in os.listdir(return_dir):
            oldj = json.load(open(nls_dir+"//"+fileName, "r"), object_pairs_hook=OrderedDict)
            newj = json.load(open(return_dir+"//"+fileName, "r"), object_pairs_hook=OrderedDict)
            compare_switch(newj, oldj)
            old = open(nls_dir+"//"+fileName, "w")
            old.write(json.dumps(oldj, indent=4))
            