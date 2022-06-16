from scapy.all import *
import numpy as np
import struct
import time

dst_addr = ('10.0.0.171', 9999) # 9998
src_addr = ('10.0.0.249', 0)


N = 20
p = 0.52

while True:
    for i in range(N):
        content_dict = {'start':'', 'end':'', 'dist':''}
        x = np.random.rand()
        if x < 0.5:
            content_dict['start'] = src_addr[0]
            content_dict['dist'] = '0'
        else:
            if content_dict['dist'] == '0': #If marked right before 
                content_dict['end'] = src_addr[0]
            if content_dict['dist'] != '': #If marked Before
                content_dict['dist'] = str(int(content_dict['dist']) + 1)
        
        a = IP(dst= dst_addr[0])/TCP(dport= dst_addr[1])/','.join([key + ':' + val for key, val in content_dict.items()])
        send(a)
    print(str(N) + ' packets sent\n Waiting...\n')
    time.sleep(1)
