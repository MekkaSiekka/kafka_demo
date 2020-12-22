import random
import json
LOCATION = ["NYC","LA","SF","ATL"]
ITEM = ["COMMODITY","ELECTRONIC","FURNITURE"]
PRICE = [1,10,100,1000,10000]

ORDERS = 10

def pick_random(L):
    return random.choice(L)

all_data = []
for _ in range(ORDERS):
    loc = pick_random(LOCATION)
    num_items = random.randint(1, 10)
    items = []
    for _ in range(num_items):
        item = pick_random(ITEM)
        price = pick_random(PRICE)
        items.append([item,price])
    print(items)
    all_data.append(items)




    
