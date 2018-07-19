import json
import os
from collections import OrderedDict
import re
   
def sync_a_tag(node, target, retranslate):
    for key in node:
        if isinstance(node[key],dict):
            if key in target:
                sync_a_tag(node[key],target[key],retranslate)
        else:
            if "<a" in node[key] and key in target:
                olds = get_a_tags(node[key])
                news = get_a_tags(target[key])
                if len(olds) == len(news):
                    for i,old in enumerate(olds):
                        if len(get_tags(get_a_content(old))) == len(get_tags(get_a_content(news[i]))):
                            node[key] = node[key].replace(get_a_tag(old),get_a_tag(news[i]),1)
                        else:
                            print(key+":"+old)
                            print(key+":"+news[i])
                            retranslate[key] = news[i]
                
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


country_codes = {"ar","cs","da","de","el","en","es","fi","fr","he","hr","hu","it","ja","ko","nb","nl","pl","pt","pt-BR","ro","ru","sk","sl","sr-Latn","sv","tr","uk","zh-hans","zh-hant"}
dirName = input("NLS directory:")
dir = os.listdir(dirName)
# read the standard file
target_js = json.load(open(dirName+"//target.json"), object_pairs_hook=OrderedDict)
retranslatej = dict()
for fileName in dir:
    if fileName.replace(".json","") in country_codes:
        # read file to be modify
        tbc_file = open(dirName+"/"+fileName, "r")
        tbc_js = json.load(tbc_file, object_pairs_hook=OrderedDict)
        sync_a_tag(tbc_js,target_js,retranslatej)
        # write the file which was modified
        tbc_file = open(dirName+"//"+fileName, "w")
        tbc_file.write(json.dumps(tbc_js, indent=4))
retranslate = open("re-translte.json","w")
retranslate.write(json.dumps(retranslatej, indent=4))

