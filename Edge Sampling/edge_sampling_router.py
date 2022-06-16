import struct
import pickle
import numpy as np
from scapy.all import *


filter_addr = ('10.0.0.249', 9999)
this_addr = ('10.0.0.231', 9999)
dst_addr = ('10.0.0.171', 9999)
N = 1
while True:
    capture = sniff(filter= 'src host ' + filter_addr[0] + ' and tcp port ' + str(filter_addr[1]), count= N)

    for pckt in capture:
        # Read Content
        vals_str = pckt['Raw'].load.decode()
        val_list = vals_str.split(',')
        content_dict = {}
        for col_val in val_list:
            col, val = col_val.split(':')
            content_dict[col] = val

        # PPM Marking
        x = np.random.rand()
        if x < 0.5:
            content_dict['start'] = this_addr[0]
            content_dict['dist'] = '0'
        else:
            if content_dict['dist'] == '0': #If marked right before 
                content_dict['end'] = this_addr[0]
            if content_dict['dist'] != '': #If marked Before
                content_dict['dist'] = str(int(content_dict['dist']) + 1)
        

        a = IP(dst= dst_addr[0])/TCP(dport= dst_addr[1])/','.join([key + ':' + val for key, val in content_dict.items()])
        send(a)