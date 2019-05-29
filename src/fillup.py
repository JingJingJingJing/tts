import os
import json
from collections import OrderedDict
from utils import codelist, loadJsonFile

def fill_up(nls, en):
    for key in en:
        if key not in nls:
            insert(nls, en, key)
        elif isinstance(en[key], dict):
            fill_up(nls[key], en[key])


def insert(node, std, key):
    after = False
    for k in std:
        if not after and k == key:
            after = True
            node[key] = std[key]
        if after and k in node:
            node.move_to_end(k)


def main():
    nls_dir = input("NLS directory:")
    en = loadJsonFile(nls_dir+"//en.json")
    for fileName in os.listdir(nls_dir):
        lang = fileName.replace(".json", "")
        if lang == "en":
            continue
        nls = loadJsonFile(nls_dir+"//"+fileName)
        fill_up(nls, en)
        stream = open(nls_dir+"//"+fileName, "w", encoding="UTF-8")
        stream.write(json.dumps(nls, indent=4, ensure_ascii=False))
