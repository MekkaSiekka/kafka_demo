import matplotlib.pyplot as plt

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import pyaudio
import wave

import sys
import os

import pickle #load train data
import json
import random #shuffle


def pretty_print(content):
    print(json.dumps(content,indent = 4))

# def plot_one_store():

dbfile = open('billing.pkl', 'rb')      
data = pickle.load(dbfile) 
dbfile.close() 

pretty_print(data)

store_dirs = os.listdir('./billings')
for store_id in data.keys():
    
    if not store_id in store_dirs:
        cmd = "mkdir ./billings/"+store_id
        os.system(cmd)
    store_dir = "./billings/"+store_id
    store_info = data[store_id]
    for month in store_info.keys():
        keys = list(store_info[month].keys())
        vals = []
        for key in keys:
            val = store_info[month][key]["total"] 
            vals.append(val)
        plt.bar(keys,vals)
        plt.savefig(store_dir+ "/"+month+ ".png", dpi=50)
        plt.clf()
    




