import pickle
from Motter import mottersim
from Ratios import ratios
import math
from networkx import *
import random


N=3000
n=20
p=0.001

G = barabasi_albert_graph(N,2)


#Select Initially removed nodes for n times, the initially removed nodes will be the same for each 1.i 

x = math.floor(N*p)

if x == 0:
    x=1

initrem=[]


for i in range(n):
    nodedeck=list(range(0,N))
    rem=[]
    for j in range(0,x):
            random.shuffle(nodedeck)      
            rem.append(nodedeck.pop())

    initrem.append(rem)


mottersim(N,n,G,initrem)

rats = ratios(20)



values=[]

for i in rats:
    x=0
    for j in i:
        x=x+j
    values.append(x)

print(initrem)

filename = 'Ratios'
outfile = open(filename,'wb')
pickle.dump(ratios,outfile)
outfile.close()

rats = ratios(N)

lam = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]

values=[]

for i in range(len(rats)):
    x=0
    for j in rats[i]:
        x=x+j
    x=x/len(rats[i])
    print(x)
    values.append(x)


filename = 'Ratios'
outfile = open(filename,'wb')
pickle.dump(ratios,outfile)
outfile.close()

plt.plot(lam,values)

plt.savefig('Motter_N='+str(N)+'.pdf')