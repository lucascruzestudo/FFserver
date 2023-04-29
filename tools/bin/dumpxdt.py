#!/usr/bin/env python3

import json
from unitypack.asset import Asset

INPUT = 'C://Users//Admin//AppData//LocalLow//Unity//Web Player//Cache//Fusionfall//tabledata_2eresourceFile//CustomAssetBundle-TableData'
OUTPUT = 'xdt1013.json'
XDTINDEX = 2139558964

def main(tabledata):
    xdtdata = tabledata.objects[XDTINDEX].read()

    out = {}
    for tname, table in xdtdata.items():
        out[tname] = {}
        try:
            for dname, data in table.items():
                out[tname][dname] = data
        except:
            out[tname] = '<err>'

    with open(OUTPUT, 'w') as f:
        json.dump(out, f, indent=4)


with open(INPUT, 'rb') as f:
    tabledata = Asset.from_file(f)
    main(tabledata)
