from flask import Flask
app = Flask(__name__)
import numpy as np
from flask import json
from flask import request
import base64
from speech import take_response, text_to_speech

listvocal = {}
dictvocal = {}

@app.route("/getSound/<word>")
def getSound(word):
    res = {"word": word}
    res["audio"] = base64.b64encode(text_to_speech(word))
    # data = base64.b64decode(res["audio"])
    # with open('output1.wav', 'wb') as out:
    #     # Write the response to the output file.
    #     out.write(data)
    #     print('Audio content written to file "output1.wav"')
    return json.dumps(res)

@app.route("/getScore", methods=["POST"])
def getScore():
    res = {}
    data = request.get_json()
    word = data['word']
    encode = data['encode']
    audiodata = base64.b64decode(encode)
    results = take_response(audiodata)
    check = False
    checksub = False
    wordBig = ""
    score = 0
    for result in results:
        if(word == result.alternatives[0].transcript.lower()):
            check = True
            score = result.alternatives[0].confidence
        elif(word in result.alternatives[0].transcript.lower()):
            checksub = True
            wordBig = result.alternatives[0].transcript.lower()
            if score == 0:
                score = result.alternatives[0].confidence
    score = int(float(score*100))
    # print(type(score))
    res["score"] = score
    res["phonetic"] = []
    res["word"] = word
    phonetics = listvocal[word].split(" ")
    for i in phonetics:
        res["phonetic"].append({i: True})
    if(not check):
        if not checksub:
            res["score"] = 0
            res["phonetic"] = []
            for i in phonetics:
                res["phonetic"].append({i: False})
        else:
            res["phonetic"] = []
            substr = wordBig.replace(word, '')
            percent = len(substr) / len(wordBig)
            num = int(len(phonetics) * percent)
            if num == 0:
                num = 1
            elif num > len(phonetics):
                num = len(phonetics)
            for i in range(0, len(phonetics)):
                if(len(phonetics) - i <= num):
                    res["phonetic"].append({phonetics[i]: False})
                else:
                    res["phonetic"].append({phonetics[i]: True})     
    htmlres = ""   
    for i in range(len(res["phonetic"])):
        # print(listvocal[word].split(" ")[i])
        if res["phonetic"][i][listvocal[word].split(" ")[i]]:
            htmlres = htmlres + "<span style=\"color:red\"><strike>" + str(listvocal[word].split(" ")[i]) + " " + "</strike> </span>"
        else:
            htmlres = htmlres + "<span style=\"color:#30FF00\">" + str(listvocal[word].split(" ")[i]) + " " + "</span>"
    res["result"] = htmlres
    return json.dumps(res)

@app.route("/getLession")
def getLession():
    reslession = []
    lession1 = {
        "id": 1,
        "name": "Explore San Francisco",
        "list_lession": [
            {
                "id":"lession11",
                "difficult": "easy",
                "name": "Lession 1 - Friday night plans",
                "url_image_lession": "https://loading.io/s/icon/lnquqt.svg",
                "vocal": dictvocal["Lession1"][0:100]
            },
            {
                "id":"lession12",
                "difficult": "difficult",
                "name": "Lession 2 - Los Angeles to San Francisco",
                "url_image_lession": "https://loading.io/s/icon/lnquqt.svg",
                "vocal": dictvocal["Lession3"][0:100]
            }
        ]
    }
    lession2 = {
        "id": 2,
        "name": "One lession per day",
        "list_lession": [
            {
                "id":"lession21",
                "difficult": "easy",
                "name": "Lession 1 - Lets get creative with a study group",
                "url_image_lession": "https://loading.io/s/icon/lnquqt.svg",
                "vocal": dictvocal["Lession2"][0:100]
            },
            {
                "id":"lession22",
                "difficult": "medium",
                "name": "Lession 2 - 10 minutes to perfection",
                "url_image_lession": "https://loading.io/s/icon/lnquqt.svg",
                "vocal": dictvocal["Lession3"][200:300]
            }
        ]
    }
    lession3 = {
        "id": 3,
        "name": "Beat the IELTS test",
        "list_lession": [
            {
                "id":"lession31",
                "difficult": "difficult",
                "name": "Lession 1 - To be awarded a scholarship",
                "url_image_lession": "https://loading.io/s/icon/lnquqt.svg",
                "vocal": dictvocal["Lession4"][100:200]
            },
            {
                "id":"lession32",
                "difficult": "difficult",
                "name": "Lession 2 - To be awarded a scholarship (harder version)",
                "url_image_lession": "https://loading.io/s/icon/lnquqt.svg",
                "vocal": dictvocal["Lession1"][300:400]
            }
        ]
    }
    reslession.append(lession1)
    reslession.append(lession2)
    reslession.append(lession3)
    response = app.response_class(
        response=json.dumps(reslession),
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
                phonetic = phonetic[0:len(phonetic)-1]
                listvocal[vocal] = phonetic
                if len(vocal) < 5:
                    dictvocal["Lession1"].append({"vocal":vocal, "phonetic":phonetic, "link": "35.247.180.113:4000/getSound/" + vocal})
                elif len(vocal) < 9:
                    dictvocal["Lession2"].append({"vocal":vocal, "phonetic":phonetic, "link": "35.247.180.113:4000/getSound/" + vocal})
                elif len(vocal) < 11:
                    dictvocal["Lession3"].append({"vocal":vocal, "phonetic":phonetic, "link": "35.247.180.113:4000/getSound/" + vocal})
                else:
                    dictvocal["Lession4"].append({"vocal":vocal, "phonetic":phonetic, "link": "35.247.180.113:4000/getSound/" + vocal})
    print(len(dictvocal["Lession1"]))
    print(len(dictvocal["Lession2"]))
    print(len(dictvocal["Lession3"]))
    print(len(dictvocal["Lession4"]))
    
    # print(listvocal)
    # print("aaaaaaaaaaaacccvvvvv".replace('ccc', ''))
    app.run(host="0.0.0.0", port=4000)