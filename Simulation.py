import math
import matplotlib.pyplot as plt
from networkx import *
import networkx.utils
import random
import os


def cassim(G, lamb,rem):
    global ded

    N= len(G)
    #N: number of nodes
    #lamb: The capacity coefficient
    #p: The ratio of removed nodes during the inital attack
    #m: number of links that will be formed during each step of Barabasi Alber


    W=[]
    ded=[]

    def randinattack(G,rem):
        #p is the ratio of the nodes that will be destroyed by the initial attack
        #Find the number of nodes that will be destroyed by the initial attack
        global ded

        Gr = G.copy()

        for i in rem:
            ded.append(i)
        
        #We picked a proportion of the nodes that will be removed initially.
        #Now, next lines will redistribute the load that they hold evenly between the neighbors.

        for i in rem:

            if len(Gr[i])==0:
                pass

            else: 

                distload = Gr.nodes[i]['load']/len(Gr[i])
                
                for j in Gr[i]:
                
                    #This loops in neighbors of node i 
                    Gr.nodes[j]['load']=Gr.nodes[j]['load']+distload

            Gr.remove_node(i)
        
        return Gr

    def propag(G):
        
        global ded
        
        Gr = G.copy()

        #Propogation of the cascade
        #We find each node which has a load larger than it's capacity
        #We distribute the load evenly between it's neighbors
        #Remove the nodes

        x=[]
        for i in Gr:
            if Gr.nodes[i]['load']>Gr.nodes[i]['cap']:
                x.append(i)
            
            
        ded.append(x)

               
        
        for i in x:
            if len(Gr[i])==0:
                Gr.remove_node(i)

            else: 
                distload = Gr.nodes[i]['load']/len(Gr[i])

                for j in Gr[i]:

                    Gr.nodes[j]['load']=Gr.nodes[j]['load']+distload

                Gr.remove_node(i)


        
        return Gr

    W.append(G)

    #Initial attack

    W.append(randinattack(G,rem))

    #Propogation of the cascade

    t=0

    while W[t].nodes != W[t+1].nodes:
        print('W['+str(t)+']')
        t+=1

        W.append(propag(W[t]))

    print(ded)

    return (W, ded)
