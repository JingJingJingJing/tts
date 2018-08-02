import json
import os
import re
from collections import OrderedDict
from utils import codelist, loadJsonFile

   
def sync_a_tag(node, target, retranslate):
    keys = list(node.keys())
    keys.extend(list(target.keys()))
    for key in keys:
        if key in node and isinstance(node[key],dict):
            if key in target:
                if key not in retranslate:
                    retranslate[key] = dict()
                sync_a_tag(node[key],target[key],retranslate[key])
        else:
            if key in target and key in node and isinstance(node[key],str) and "<a" in target[key]:
                olds = get_a_tags(node[key])
                news = get_a_tags(target[key])
                if len(olds) == len(news):
                    for i,old in enumerate(olds):
                        if len(get_tags(get_a_content(old))) == len(get_tags(get_a_content(news[i]))):
                            node[key] = node[key].replace(get_a_tag(old),get_a_tag(news[i]),1)
                        else:
                            if key not in retranslate:
                                retranslate[key] = target[key]
                else:
                    if key not in retranslate:
                        retranslate[key] = target[key]
            elif key in target and key not in node:
                if key not in retranslate:
                    retranslate[key] = target[key]
            elif key not in target and key in node:
                node.pop(key)
                
def get_tags(s):
    pattern = re.compile("(<.*?>)")
    return re.findall(pattern,s)

def get_a_tags(s):
    pattern = re.compile("(<a.*?>.*?</a>)")
    return re.findall(pattern,s)

def get_a_tag(s):
    pattern = re.compile("(<a.*?>).*?</a>")
    result = re.findall(pattern,s)
    if len(result) > 0:
        return result[0]
    else:
        return ""

def get_a_content(s):
    pattern = re.compile("<a.*?>(.*?)</a>")
    result = re.findall(pattern,s)
    if len(result) > 0:
        return result[0]
    else:
        return ""

def clearEmpty(jsonObj):
    keys = list(jsonObj.keys())
    for key in keys:
        if isinstance(jsonObj[key],dict) and len(list(jsonObj[key].keys())) <= 0:
            jsonObj.pop(key)

def main():
    dirName = input("NLS directory:")
    dir = os.listdir(dirName)
    # read the standard file
    target_js = loadJsonFile(dirName+"//en.json")
    retranslatej = OrderedDict()
    for fileName in dir:
        if fileName.replace(".json","") in codelist:
            # read file to be modify
            node = loadJsonFile(dirName+"/"+fileName)
            sync_a_tag(node,target_js,retranslatej)
            #TODO delete keys
            # write the file which was modified
            tbc_file = open(dirName+"//"+fileName, "w", encoding="UTF-8")
            tbc_file.write(json.dumps(node, indent=4, ensure_ascii=False))
    clearEmpty(retranslatej)
    retranslate = open("re-translte.json", "w", encoding="UTF-8")
    retranslate.write(json.dumps(retranslatej, indent=4))