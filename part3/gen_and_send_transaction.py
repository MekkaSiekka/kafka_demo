import random
import json

import uuid 

import pickle

from kafka import KafkaProducer

#generate transaction and push to first topic
producer = KafkaProducer(bootstrap_servers='localhost:9092')


LOCATION = ["NYC","LA","SF","ATL"]
ITEM = ["COMMODITY","ELECTRONIC","FURNITURE"]
PRICE = [1,10,100,1000,10000]
ORDERS = 10
NUM_ITEM = 5
NUM_STORE = 3

def pick_random(L):
    return random.choice(L)


'''
{
    store: store
    transaction: 
        "id":{
            "type"
            "number":
            "price"
        }
}
'''
def mock_transaction_from_store(store):
    items = store['items']
    keys = list(items.keys())
    random.shuffle(keys)
    transaction = {}
    transaction["store_id"] = store["id"]
    transaction["receipt"] = []
    for idx in range(10):
        item_key = keys[idx]
        item = items[item_key]
        one_trans = {
            "item_id" : item_key,
            "type" : item["type"],
            "price" : item["price"],
            "number" : random.randint(1,10)
        }
        transaction['receipt'].append(one_trans)
    return transaction

def gen_transactions(store_data):
    #for all months in the 
    transaction = {}
    for month in range(12):
        transaction["month"] = month
        for _ in range(100):    
            store = pick_random(store_data)
            transaction = mock_transaction_from_store(store)
            print(json.dumps(transaction,indent = 4))
            


def determine_transaction_valid(transaction):
    valid_transaction = [True,False]
    return True
    return pick_random(valid_transaction)




def process_transaction(transaction):
    is_valid = determine_transaction_valid(transaction)
    if (is_valid):
        print("sending")
        string = json.dumps(transaction)
        print(string)
        future = producer.send('sample', string.encode('UTF-8'))
        try:
            record_metadata = future.get()
        except KafkaError:
            log.exception()
            pass
    else: #if not valid, then return to the vender
        pass 


dbfile = open('stores'+'.pkl', 'rb')      
store_data = pickle.load(dbfile) 
dbfile.close() 

transactions = gen_transactions(store_data)
exit()
# json_str = json.dumps(all_transactions,indent=4)
# print(json_str)
# json_obj = json.loads(json_str)
# print(json_str)
for transaction in all_transactions:
    process_transaction(transaction)
    