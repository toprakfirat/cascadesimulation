from networkx import *
from Simulation import cassim
import matplotlib.pyplot as plt
import pickle
import os
import tqdm as tqdm

def mottersim(N,n,G,initrem):

    #N is the number of nodes
    #n is the number of instances that the simulation will be runned


    lam = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]

    
    #Total Load Finder and capacity finder

    for i in G:
        
        G.nodes[i]['inload']=0
        

    for i in tqdm.tqdm(range(len(G))):
        for j in G:
            if i == j:
                pass
            else: 
                shopats=[p for p in all_shortest_paths(G,i,j)]
                patnum= len(shopats)
                for shopat in shopats:
                    for k in shopat[1:]:
                        G.nodes[k]['inload']=G.nodes[k]['inload']+(1/patnum)

    for j in tqdm.tqdm(lam):
        
        sim=[]

        for i in G:
            G.nodes[i]['load']=G.nodes[i]['inload']
            G.nodes[i]['cap']=G.nodes[i]['inload']*j


        # fix a lambda, for every instance n_i we pick a new set of initially removed nodes

        for i in range(n):
            H = cassim(G,j,initrem[i])
            sim.append(H)

        filename = 'Simulation.'+str(j)
        outfile = open(filename,'wb')
        pickle.dump(sim,outfile)
        outfile.close()

    #We have generated the data with n instances and N many nodes. 
    #Now we will gather the data and the ratio N1/N

    for j in lam:
        
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
        

    
