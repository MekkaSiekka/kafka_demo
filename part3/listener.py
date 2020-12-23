
from kafka import KafkaConsumer


import uuid 

import pickle

import json

import collections


def pretty_print(content):
    print(json.dumps(content,indent = 4))

def is_valid(transaction):
    return False
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('sample',
                         bootstrap_servers=['localhost:9092'])


'''
{
    "month": 12,
    "store_id": "301e9556-44e4-11eb-9c8c-acde48001122",
    "receipt": [
        {
            "item_id": "301e9830",
            "type": "FURNITURE",
            "price": 100,
            "number": 10
        }
    ]
}
'''
data = collections.defaultdict()
data = {}
for message in consumer:
    transaction = message.value.decode('utf-8')
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`

    # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                       message.offset, message.key,
    #                                       message.value))
    #print(transaction)  #item_id, type, price, amount
    transaction = json.loads(transaction)
    is_valid(transation)
    store_id = transaction["store_id"]
    month = str(transaction['month'])
    for item in transaction["receipt"]:
        item_id = item["item_id"]
        price = item["price"]
        number = item["number"]
        if not store_id in data.keys():
            data[store_id] = {}
            for m in range(0,12):
                data[store_id][str(m+1)] = {}
            print(item_id)
        if not item_id in data[store_id][month].keys():
                data[store_id][month][item_id] = 0
        data[store_id][month][item_id] += price*number
    pretty_print(data)





