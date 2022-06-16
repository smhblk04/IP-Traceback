import struct
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import importlib
from scapy.all import *
ps = importlib.import_module("basic-parse-packet-sniffer-linux")


filter_addr = '10.0.0.249'
true_addr = '10.0.0.249'
N = 50
t_df = pd.DataFrame(columns=['start', 'end', 'dist'])

capture = sniff(filter= 'src host ' + filter_addr + ' and tcp port 9999', count= N)
capture.summary()

for pckt in capture:
    vals_str = pckt['Raw'].load.decode()
    val_list = vals_str.split(',')
    row_dict = {}
    for col_val in val_list:
        col, val = col_val.split(':')
        row_dict[col] = val
    t_df.loc[t_df.shape[0]] = row_dict
print(t_df)