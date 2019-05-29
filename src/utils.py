import json
from collections import OrderedDict

codelist = {'ar','cs','da','de','el','es','fi','fr','he','hr','hu','it','ja','ko','nb','nl','pl','pt','pt-BR','ro','ru','sk','sl','sr','sv','tr','uk','zh-Hans','zh-Hant'}

def loadJsonFile(dir):
    with open(dir, 'r', encoding='UTF-8') as file:
        content = file.read()
        if content.startswith(u'\ufeff'):
            content = content.encode('UTF-8')[3:].decode('UTF-8')
        return json.loads(content, object_pairs_hook=OrderedDict)

def loadTxtFile(dir):
    with open(dir, 'r', encoding='UTF-8') as file:
        content = file.read()
        if content.startswith(u'\ufeff'):
            content = content.encode('UTF-8')[3:].decode('UTF-8')
        return content