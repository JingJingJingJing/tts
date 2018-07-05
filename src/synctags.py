import json
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

node = json.load(open("src//test.json"),object_pairs_hook=OrderedDict)
target = json.load(open("src//target.json"),object_pairs_hook=OrderedDict)
synca(node, target)
out = open("t.json","w")
out.write(json.dumps(node, indent=4))
out.close()
