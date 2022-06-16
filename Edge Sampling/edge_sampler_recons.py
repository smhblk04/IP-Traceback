import matplotlib.pyplot as plt
import numpy as np
import pickle
import pandas as pd
import networkx as nx

with open('edge_samp1.pickle', 'rb') as f:
    t_df = pickle.load(f)

print(t_df)

# Path Reconstruction
root = '10.0.0.171'

G = nx.DiGraph()
G.add_node(root)

for index, row in t_df.iterrows():
    if row['dist'] == '':
        continue
    if int(row['dist']) == 0:
        G.add_edge(row['start'], root, dist= 0)
    else:
        G.add_edge(row['start'], row['end'], dist= row['dist'])

nx.draw(G, with_labels= True)
plt.show()
