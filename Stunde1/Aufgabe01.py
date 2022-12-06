import random
def ziehzahlen(start,end, zieh):
    zahlen=[]
    for x in range(start,end+1):
        zahlen.append(x)
    #zahlenGezogen = []
    gezogen = 0

    for x in range(zieh):
        stelle = random.randint(0, len(zahlen)-1-gezogen)
        gezogen += 1

        zahlen[stelle],zahlen[len(
            zahlen)-1-x] = zahlen[len(zahlen)-1-x],zahlen[stelle]
    #print(zahlen)
    return zahlen[-zieh:] #bzw [-7:-1]

print(ziehzahlen(0,45,6))