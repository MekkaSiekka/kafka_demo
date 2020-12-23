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
TRANSACTION_PER_STORE = 10
TRNASACTION_PER_MONTH = 100

def pretty_print(content):
    print(json.dumps(content,indent = 4))

def pick_random(L):
    return random.choice(L)

def mock_transaction_from_store(store):
    items = store['items']
    keys = list(items.keys())
    random.shuffle(keys)
    transaction = {}
    transaction["store_id"] = store["id"]
    transaction["receipt"] = []
    for idx in range(TRANSACTION_PER_STORE):
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
    all_transactions = []
    for month in range(1,13):
        for _ in range(TRNASACTION_PER_MONTH):   
            transaction = {}
            transaction["month"] = month 
            store = pick_random(store_data)
            
            store_transaction = mock_transaction_from_store(store)
            #print("one store")
            pretty_print(store_transaction)
            for obj in store_transaction.keys():
                transaction[obj] = store_transaction[obj]
            #print(transaction)
            all_transactions.append(transaction)
    #print(json.dumps(all_transactions,indent = 4))
    all_transactions.append({"month":13})
    return all_transactions       


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
#pretty_print(store_data)
dbfile.close() 
all_transactions = gen_transactions(store_data)
all_transactions
#pretty_print(all_transactions)
for transaction in all_transactions:
    process_transaction(transaction)
    