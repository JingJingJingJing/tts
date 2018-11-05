import os
import utils
import json
from collections import OrderedDict

sectionMap = {'Antivirus': "av", 'Wifi Security': 'ws', 'zhangling': 'zhangling'}

def getTitle(title):
    return title.replace('-','').strip()

def splitKeyValue(s):
    it = iter(s)
    key = ''
    a = next(it)
    while a:
        if a == ':':
            break
        key += a
        a = next(it)
    return [key, s[len(key)+1:len(s)]]

def txt2Json(txtDir):
    content = utils.loadTxtFile(txtDir).split('\n')
    jsonList = list()
    it = iter(content)
    title = getTitle(next(it))
    try:
        while title:
            if title in sectionMap:
                json = OrderedDict()
                jsonList.append(json)
                json[sectionMap[title]] = OrderedDict()
                json = json[sectionMap[title]]
                s = next(it)
                while getTitle(s) not in sectionMap:
                    if(s):
                        keyValueList = splitKeyValue(s)
                        json[keyValueList[0].strip('\"')] = keyValueList[1].strip().strip(',').strip('"').replace('\\\"', '"')
                    s = next(it)
                title = getTitle(s)
            else:
                title = next(it)
    except StopIteration:
        pass
    return jsonList

def main():
    txt_dir = input('txt directory:')
    for key in sectionMap.keys():
        if not os.path.isdir(txt_dir + '/' + key):
            os.mkdir(txt_dir + '/' + key)
    for fileName in os.listdir(txt_dir):
        if fileName.endswith('.txt'):
            code = fileName.replace('.txt','')
            jsonList = txt2Json(txt_dir+'/'+fileName)
            for key,j in zip(sectionMap.keys(),jsonList):
                jsonFile = open(txt_dir + '/' + key + "/" + code + '.json', 'w', encoding='UTF-8')
                jsonFile.write(json.dumps(j, indent=4, ensure_ascii=False))