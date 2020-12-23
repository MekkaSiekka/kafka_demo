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
NUM_ITEM = 100
NUM_STORE = 5

def pick_random(L):
    return random.choice(L)

#for one store, generate all items in the streo as well as basic info
def gen_store_items():
    ret = {}
    loc = pick_random(LOCATION)
    ret["location"] = loc
    store_id = str(uuid.uuid1())
    ret["id"] = store_id   
    items = {}
    for _ in range(NUM_ITEM):
        #print (uuid.uuid1()) 
        item_type = pick_random(ITEM)
        price = pick_random(PRICE)
        item_id = str(uuid.uuid1())[0:8]
        items[item_id] = {
            "type" : item_type,
            "price": price
        }
    ret["items"] = items
    print(ret)
    #print(ret)
    return ret


'''
{
    
}
'''

def gen_store_data():
    ret = []
    for _ in range(NUM_STORE):
        ret.append(gen_store_items())
    return ret





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

store_data = gen_store_data()
print(json.dumps(store_data,indent=4))

dbfile = open('stores'+'.pkl', 'wb') 
# source, destination 
pickle.dump(store_data, dbfile)                      
dbfile.close()


exit()

all_transactions = gen_data()
# json_str = json.dumps(all_transactions,indent=4)
# print(json_str)
# json_obj = json.loads(json_str)
# print(json_str)
for transaction in all_transactions:
    process_transaction(transaction)
    




    
