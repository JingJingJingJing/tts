import json
import sys
import io
   
def synca(node):
    for key in node:
        if isinstance(node[key],dict):
            sync(node[key])
        else:
            if "<a" in node[key]:
                print(node[key])
                print(" ")
        
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
en = open("src//test.json", encoding='utf-8')
synca(json.load(en))