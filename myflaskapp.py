
from flask import Flask, request, redirect
from pymongo import MongoClient
import logging

logs=logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/test')
def test():
    return "Test application"


@app.route('/')
def alpha():
    # Module to Obtain the paramter from the Database.
    if 'key' in request.args:
        key = request.args.get('key')
        obj_id = getRecord(key)
        link = obj_id.get('value')
        return redirect("https://"+link)
    else:
        return "No input specified"

@app.route('/add')
def beta():
    # Module to load the parameter to the Database.
    if 'key' in request.args:
        key = request.args.get('key')
        value = request.args.get('value')
        obj_id = addRecord(key, value)
        return "Value Added to the Database : " + str(obj_id)
    else:
        return "No input specified"

def addRecord(name, link):
    client = MongoClient("mongodb://golink_mongodb_2:27017")
    logs.debug(client)
    db = client.Test
    addStr = {"key": name ,"value": link}
    print '------------------------'
    print addStr
    result = db.godataset.insert_one(addStr)
    client.close()
    return result.inserted_id


def getRecord(name):
    client = MongoClient("mongodb://golink_mongodb_2:27017")
    logs.debug(client)
    db = client.Test
    findStr = {"key":name}
    result = db.godataset.find_one(findStr)
    client.close()
    return result

if __name__=='__main__':
        app.run(debug=True, port=3134)
