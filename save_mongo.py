from config import MONGO_URL, MONGO_NAME
from pymongo import MongoClient

client = MongoClient(MONGO_URL)
db = client[MONGO_NAME]

def save_to_mongo(data):
    if db['position'].update({'positionName': data['positionName'], 'companyName': data['companyFullName']},
                             {'$set': data}, True):
        print('%s %s save to mongo success!' % (data['positionName'], data['companyFullName']))
    else:
        print('save to mongo fail!')