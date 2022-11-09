import datetime
import os
import json


def post2db(data):
    subjectName = str(data["subjectName"])
    subjectID = int(data["subjectID"])
    songID = int(data["songID"])
    arousalOrValence = ""
    arousal = data["arousal"]
    arousal_time = data["arousal_time"]
    valence = data["valence"]
    valence_time = data["valence_time"]
    ibi = data["ibi"]
    ibi_time = data["ibi_time"]
    bvp = data["bvp"]
    bvp_time = data["bvp_time"]
    gsr = data["gsr"]
    gsr_time = data["gsr_time"]
    temp = data["temp"]
    temp_time = data["temp_time"]
    subjectAge = data["subjectAge"]
    
    if data["isValence"]:
        arousalOrValence = "valence"
    else:
        arousalOrValence = "arousal"

    #createdATはUTCタイムゾーンで取るため、日本時間とは九時間ずれてる
    dt_now = datetime.datetime.now()
    createdAt = f"{dt_now.year}_{dt_now.month}_{dt_now.day}_{dt_now.hour}_{dt_now.minute}_{dt_now.second}"
    print(dt_now.year)

    doc_name = f"{subjectID}-{songID}-{createdAt}-{arousalOrValence}" 

    #ここでのディレクトリを作る部分は、事前にディレクトリ作成用のスクリプト(scriptFoMkdir.py)を使えばいらない。
    os.chdir('data')
    os.makedirs(str(songID), exist_ok=True)
    os.chdir('..')
    filename = 'data/' + str(songID) + '/' + doc_name + '.json'
    f = open(filename, 'w')

    
    content = { 
        'subjectName':subjectName,
        'age':subjectAge,
        'subjectID':subjectID,
        'songID':songID,
        'arousal':arousal,
        'arousal_time':arousal_time,
        'valence':valence,
        'valence_time':valence_time,
        'ibi':ibi,
        'ibi_time':ibi_time,
        'bvp':bvp,
        'bvp_time':bvp_time,
        'gsr':gsr,
        'gsr_time':gsr_time,
        'temp':temp,
        'temp_time':temp_time,
        'createdAt':createdAt
    }

    content_json = json.dumps(content)
    

    f.write(content_json)
    f.close
    return True

def getMusicList(numberOfMusics):
    files = './MusicDictionary.csv'
    f = open(files, 'r')
    data = f.read()
    f.close()
    lst1 = data.split(',')

    musicList = []

    musicDict = {}
    for lst in lst1:
        DIR = './data/' + lst
        numberOfAnnotation = sum(os.path.isfile(os.path.join(DIR, name)) for name in os.listdir(DIR))
        musicDict[lst] = numberOfAnnotation
    

    musicDict = sorted(musicDict.items(),key=lambda x:x[1])
    musicDict = dict((x, y) for x, y in musicDict)

    musicList = list(musicDict.keys())

    musicListByNumberStr = []
    for i in range(numberOfMusics):
        musicListByNumberStr.append(musicList[i])

    musicListByNumber = [int(s) for s in musicListByNumberStr]
    return musicListByNumber
