from flask import Flask
from flask import request
import json
from flask import jsonify
import connectdb

app = Flask(__name__)

@app.route('/post_data', methods=['POST'])
def check():
    data = request.get_data().decode('utf-8')
    data = json.loads(data)
    if connectdb.post2db(data):
        return "OK"


@app.route('/musicListForSubject', methods=['GET'])
def getList():
    content = request.args.get('numberOfMusics')
    musicList = connectdb.getMusicList(int(content))
    contents = {"musicList": musicList}
    return jsonify(contents)



