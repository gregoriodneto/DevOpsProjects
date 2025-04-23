from flask import Flask
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://mongodb:27017/")
db = client.testdb

@app.route("/")
def hello():
    db.test.insert_one({"msg": "Olá do Python!"})
    return "Olá do Python com MongoDB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)