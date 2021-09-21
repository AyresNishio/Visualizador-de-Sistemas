
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from numpy.core.fromnumeric import size


# IEEE 14-BUS POWER SYSTEM
# Ybus = np.loadtxt("ieee-14-bus.txt", dtype='i', delimiter='\t')
# coord = {
# 0: np.array([0, 4]), 
# 1: np.array([0, 2]), 
# 2: np.array([0, 0]), 
# 3: np.array([6, 0]), 
# 4: np.array([6, 2]), 
# 5: np.array([2, 2]), 
# 6: np.array([0, 6]), 
# 7: np.array([4, 4]), 
# 8: np.array([2, 4]), 
# 9: np.array([6, 6]), 
# 10: np.array([4, 6]), 
# 11: np.array([2, 6]), 
# 12: np.array([0, 8]), 
# 13: np.array([2, 8]), 
# 14: np.array([6, 8])}

# Barras = range(1,np.size(Ybus,0))
# S1 = np.array([1,2,3,5])
# S2 = np.array([4,7,8,9])
# S3 = np.array([6,10,11,12,13,14])

# IEEE 30-BUS POWER SYSTEM
# Ybus = np.loadtxt("ieee-30-bus-mod.txt", dtype='i', delimiter='\t')
# k = 30
# coord = {
# 0: np.array([ 15, 12]),
# 1: np.array([ -2, 10]),
# 2: np.array([ 4, 10]),
# 3: np.array([ -2,  8]),
# 4: np.array([ 4,  8]),
# 5: np.array([ 8, 10]),
# 6: np.array([ 8,  8]),
# 7: np.array([12, 10]),
# 8: np.array([12,  8]),
# 9: np.array([ 8,  4]),
# 10: np.array([ 6,  4]),
# 11: np.array([10,  4]),
# 12: np.array([ 0,  4]),
# 13: np.array([ -2,  6]),
# 14: np.array([ 0,  2]),
# 15: np.array([ -2,  0]),
# 16: np.array([ 2,  4]),
# 17: np.array([ 4,  4]),
# 18: np.array([ 2,  2]),
# 19: np.array([ 4,  2]),
# 20: np.array([ 6,  2]),
# 21: np.array([10,  2]),
# 22: np.array([ 8,  2]),
# 23: np.array([ 2,  0]),
# 24: np.array([ 4,  0]),
# 25: np.array([ 6,  0]),
# 26: np.array([ 8,  0]),
# 27: np.array([12,  4]),
# 28: np.array([12,  6]),
# 29: np.array([10,  0]),
# 30: np.array([12,  2])}

Ybus = np.loadtxt("ieee-118-bus.txt", dtype='i', delimiter=",")
coord = {
1: np.array([15, 0]),
2: np.array([130, 0]),
3: np.array([15, -40]),
4: np.array([40, -60]),
5: np.array([15, -100]),
6: np.array([80, -100]),
7: np.array([130, -80]),
8: np.array([30, -160]),
9: np.array([30, -220]),
10: np.array([30, -280]),
11: np.array([80, -60]),
12: np.array([130, -40]),
13: np.array([180, -75]),
14: np.array([220, -15]),
15: np.array([220, -75]),
16: np.array([130, -130]),
17: np.array([170, -130]),
18: np.array([215, -130]),
19: np.array([275, -100]),
20: np.array([260, -160]),
21: np.array([260, -210]),
22: np.array([260, -285]),
23: np.array([260, -335]),
24: np.array([285, -235]),
25: np.array([260, -390]),
26: np.array([185, -310]),
27: np.array([60, -255]),
28: np.array([60, -190]),
29: np.array([60, -130]),
30: np.array([185, -230]),
31: np.array([145, -175]),
32: np.array([100, -220]),
33: np.array([300, -45]),
34: np.array([340, -100]),
35: np.array([295, -70]),
36: np.array([295, -145]),
37: np.array([370, -45]),
38: np.array([355, -220]),
39: np.array([300, 0]),
40: np.array([340, 0]),
41: np.array([390, -30]),
42: np.array([410, 0]),
43: np.array([320, -165]),
44: np.array([390, -70]),
45: np.array([390, -145]),
46: np.array([390, -190]),
47: np.array([440, -150]),
48: np.array([425, -85]),
49: np.array([475, -135]),
50: np.array([470, -80]),
51: np.array([500, -105]),
52: np.array([465, -40]),
53: np.array([430, 0]),
54: np.array([495, 0]),
55: np.array([585, 0]),
56: np.array([510, -40]),
57: np.array([525, -90]),
58: np.array([545, -50]),
59: np.array([560, -30]),
60: np.array([600, -60]),
61: np.array([585, -125]),
62: np.array([600, -180]),
63: np.array([585, -70]),
64: np.array([560, -125]),
65: np.array([580, -200]),
66: np.array([500, -180]),
67: np.array([600, -245]),
68: np.array([477, -250]),
69: np.array([440, -200]),
70: np.array([380, -235]),
71: np.array([285, -330]),
72: np.array([285, -285]),
73: np.array([285, -390]),
74: np.array([310, -350]),
75: np.array([345, -330]),
76: np.array([400, -330]),
77: np.array([450, -330]),
78: np.array([415, -250]),
79: np.array([455, -270]),
80: np.array([490, -290]),
81: np.array([535, -270]),
82: np.array([400, -365]),
83: np.array([345, -365]),
84: np.array([290, -430]),
85: np.array([345, -415]),
86: np.array([345, -490]),
87: np.array([310, -490]),
88: np.array([390, -385]),
89: np.array([390, -490]),
90: np.array([440, -490]),
91: np.array([480, -490]),
92: np.array([470, -415]),
93: np.array([415, -425]),
94: np.array([490, -370]),
95: np.array([415, -385]),
96: np.array([500, -330]),
97: np.array([465, -330]),
98: np.array([515, -330]),
99: np.array([535, -290]),
100: np.array([560, -325]),
101: np.array([505, -415]),
102: np.array([495, -490]),
103: np.array([535, -415]),
104: np.array([585, -365]),
105: np.array([600, -330]),
106: np.array([528, -245]),
107: np.array([580, -240]),
108: np.array([600, -410]),
109: np.array([600, -490]),
110: np.array([555, -490]),
111: np.array([510, -490]),
112: np.array([575, -400]),
113: np.array([150, -235]),
114: np.array([130, -320]),
115: np.array([130, -390]),
116: np.array([475, -170]),
117: np.array([200, 0]),
118: np.array([370, -270])}

#Grupo 1
with open('Grupo1.txt', 'r') as f:
    S1 = np.array([int(b)  for b in f])
#print(G1)

#Grupo 2
with open('Grupo2.txt', 'r') as f:
    S2 = np.array([int(b)  for b in f])
#print(G2)

#Grupo 3
with open('Grupo3.txt', 'r') as f:
    S3 = np.array([int(b)  for b in f])


def Monta_sys(Ss,Ybus):

    G = nx.Graph()

    for v in Ss:
        G.add_node(v)

    for i in Ss:
        for j in Ss:
            if (i>j)  and (Ybus[i-1, j-1]) == 1:
               G.add_edge(i,j)

    return G    

def Display_sys(G,coord,color):

    v_labels = {x: x for x in G.nodes}

    nx.draw_networkx_labels(G, coord, v_labels, font_size=11, font_color='w', font_family = "Tahoma", font_weight = "normal")
    nx.draw_networkx_nodes(G, coord, node_size = 300, node_color=color, alpha=1, node_shape='o')
    nx.draw_networkx_edges(G, coord, edge_color = color)

def Display_not_found_Cks(NFC_file_name,color):
    NFC = []


    with open(NFC_file_name, 'r') as f:
        for line in f:
            NFC.append([int(num) for num in line.split(' ')])


    Cflux = nx.Graph()
    Cinjs = nx.Graph()
    for i in NFC:
        if size(i) == 2:
            Cflux.add_edge(i[0],i[1])
        if size(i) == 1:
            Cinjs.add_node(i[0])


    nx.draw_networkx_nodes(Cinjs, coord, node_shape='s', node_color = color,node_size=500)

    nx.draw_networkx_edges(Cflux, coord, style='dashed', edge_color = color, width=3)       
 

# G  = Monta_sys(range(1,np.size(Ybus,0)+1),Ybus)
# G1 = Monta_sys(S1,Ybus)
# G2 = Monta_sys(S2,Ybus)
# G3 = Monta_sys(S3,Ybus)

# Display_sys(G, coord,'black')


# Display_sys(G1,coord,'green')
# Display_sys(G2,coord,'red')
# Display_sys(G3,coord,'orange')

# # with open('G12.txt', 'r') as f:
# #     S12 = np.array([int(b)  for b in f])

# # with open('G13.txt', 'r') as f:
# #     S13 = np.array([int(b)  for b in f])

# # with open('G23.txt', 'r') as f:
# #     S23 = np.array([int(b)  for b in f])

# Display_not_found_Cks('NFC51.txt','purple')



# #fig, axes = plt.subplots(5, 5, figsize=(12, 10))
# plt.show()

