from flask import Flask
app = Flask(__name__)
import numpy as np
from flask import json

listvocal = []
dictvocal = {}
reslession = []

@app.route("/getLession")
def getLession():
    lession1 = {
        "id": 1,
        "name": "Explore San Francisco",
        "list_lession": [
            {
                "id":"lession11",
                "difficult": "easy",
                "name": "Lession 1 - Friday night plans",
                "url_image_lession": "https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwidvPfoz_TiAhUKat4KHRiXCiQQjRx6BAgBEAU&url=https%3A%2F%2Floading.io%2Ficon%2Flnquqt-android-mobile-app-developer-programmer-coder-phone-device&psig=AOvVaw0JTeRbR7qo_3zYcrzTUKfb&ust=1561002017426893",
                "vocal": dictvocal["Lession1"][0:100]
            },
            {
                "id":"lession12",
                "difficult": "difficult",
                "name": "Lession 2 - Los Angeles to San Francisco",
                "url_image_lession": "https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwidvPfoz_TiAhUKat4KHRiXCiQQjRx6BAgBEAU&url=https%3A%2F%2Floading.io%2Ficon%2Flnquqt-android-mobile-app-developer-programmer-coder-phone-device&psig=AOvVaw0JTeRbR7qo_3zYcrzTUKfb&ust=1561002017426893",
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
                "url_image_lession": "https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwidvPfoz_TiAhUKat4KHRiXCiQQjRx6BAgBEAU&url=https%3A%2F%2Floading.io%2Ficon%2Flnquqt-android-mobile-app-developer-programmer-coder-phone-device&psig=AOvVaw0JTeRbR7qo_3zYcrzTUKfb&ust=1561002017426893",
                "vocal": dictvocal["Lession2"][0:100]
            },
            {
                "id":"lession22",
                "difficult": "medium",
                "name": "Lession 2 - 10 minutes to perfection",
                "url_image_lession": "https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwidvPfoz_TiAhUKat4KHRiXCiQQjRx6BAgBEAU&url=https%3A%2F%2Floading.io%2Ficon%2Flnquqt-android-mobile-app-developer-programmer-coder-phone-device&psig=AOvVaw0JTeRbR7qo_3zYcrzTUKfb&ust=1561002017426893",
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
                "url_image_lession": "https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwidvPfoz_TiAhUKat4KHRiXCiQQjRx6BAgBEAU&url=https%3A%2F%2Floading.io%2Ficon%2Flnquqt-android-mobile-app-developer-programmer-coder-phone-device&psig=AOvVaw0JTeRbR7qo_3zYcrzTUKfb&ust=1561002017426893",
                "vocal": dictvocal["Lession4"][100:200]
            },
            {
                "id":"lession32",
                "difficult": "difficult",
                "name": "Lession 2 - To be awarded a scholarship (harder version)",
                "url_image_lession": "https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwidvPfoz_TiAhUKat4KHRiXCiQQjRx6BAgBEAU&url=https%3A%2F%2Floading.io%2Ficon%2Flnquqt-android-mobile-app-developer-programmer-coder-phone-device&psig=AOvVaw0JTeRbR7qo_3zYcrzTUKfb&ust=1561002017426893",
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
                listvocal.append([vocal, phonetic])
                if len(vocal) < 5:
                    dictvocal["Lession1"].append({"vocal":vocal, "phonetic":phonetic})
                elif len(vocal) < 9:
                    dictvocal["Lession2"].append({"vocal":vocal, "phonetic":phonetic})
                elif len(vocal) < 11:
                    dictvocal["Lession3"].append({"vocal":vocal, "phonetic":phonetic})
                else:
                    dictvocal["Lession4"].append({"vocal":vocal, "phonetic":phonetic})
    print(len(dictvocal["Lession1"]))
    print(len(dictvocal["Lession2"]))
    print(len(dictvocal["Lession3"]))
    print(len(dictvocal["Lession4"]))
    app.run(host="0.0.0.0", port=4000)