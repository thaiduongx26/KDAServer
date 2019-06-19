from flask import Flask
app = Flask(__name__)
import numpy as np
from flask import json

listvocal = []
dictvocal = {}

@app.route("/getLession")
def getLession():
    response = app.response_class(
        response=json.dumps(dictvocal),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    filepath = 'TIMITDIC.TXT'  
    dictvocal["Lession1"] = []
    dictvocal["Lession2"] = []
    dictvocal["Lession3"] = []
    dictvocal["Lession4"] = []
    with open(filepath) as fp:  
        line = fp.readline()
        while line:
            line = fp.readline()
            if line != '':
                vocal, phonetic = line.split("  ")
                listvocal.append([vocal, phonetic])
                if len(vocal) < 5:
                    dictvocal["Lession1"].append(vocal)
                elif len(vocal) < 9:
                    dictvocal["Lession2"].append(vocal)
                elif len(vocal) < 11:
                    dictvocal["Lession3"].append(vocal)
                else:
                    dictvocal["Lession4"].append(vocal)
    print(len(dictvocal["Lession1"]))
    print(len(dictvocal["Lession2"]))
    print(len(dictvocal["Lession3"]))
    print(len(dictvocal["Lession4"]))
    app.run(port=4000)