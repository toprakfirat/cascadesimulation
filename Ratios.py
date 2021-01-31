import pickle
import os
import networkx as nx
import matplotlib.pyplot as plt


def ratios(N):

    lam = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]

    ratios=[]

    for j in lam:
        larcom=[]
        ratdec=[]

        infile = open('Simulation.'+str(j),'rb')
        data = pickle.load(infile)
        infile.close()

        for i in range(len(data)):
            x = data[i][0][len(data[i][0])-1]
            gcc = sorted(nx.connected_components(x), key=len, reverse=True)
            if len(gcc)==0:
                N2=0

            else:
                N2=len(sorted(nx.connected_components(x), key=len, reverse=True)[0])
            
            larcom.append(N2)

        for k in larcom:

            ratdec.append(k/N)

        ratios.append(ratdec)

    return(ratios)
