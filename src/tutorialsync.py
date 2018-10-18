import os
import utils
import json
from collections import OrderedDict

def main():
    template = utils.loadJsonFile("tutorial-template.json")
    t_dir = input('tutorial directory:')
    sync_key = 'title'
    sync_part = template[sync_key]
    for fileName in os.listdir(t_dir):
        j = utils.loadJsonFile(t_dir + "/" + fileName)
        tutorial = j['tutorial']
        j[sync_key] = OrderedDict()
        sync = j[sync_key]
        for key in sync_part:
            if key == 'AppsandOffers':
                sync[key] = tutorial['AppsAndOffers']
            else:
                sync[key] = tutorial[key]
        jsonFile = open(t_dir + "/" + fileName, 'w', encoding='UTF-8')
        jsonFile.write(json.dumps(j, indent=4, ensure_ascii=False))

main()
    
