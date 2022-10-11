import random
import numpy as np



def zahlen_ziehen(start, end, anz):
    all = np.arange(start, end+1)
    random.shuffle(all)
    return all[0:anz]





def statistik(start, end, anz):
    d = dict.fromkeys(np.arange(start, end+1), 0)
    for i in range(anz):
        d[int(random.random()*end + 1)] += 1
    return d

def statistik_2(start, end, anz):
    mdic = {}
    for i in range(end):
        
        mdic[i] = 0


print(zahlen_ziehen(1,45,6))
print(zahlen_ziehen(1,45,1000))
print(statistik(1,45,6))
print(statistik_2(1,45,6))