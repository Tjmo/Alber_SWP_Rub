import numpy as np
import random

global karten
karten = []

for i in range(52):
    karten.append(i)


def zahlen(random_karten):
    werte = []
    for i in range(5):
        werte.append(random_karten[i] % 13)
    return werte


def farbe(zufaelligekarte):
    farbe = []
    for i in range(5):
        farbe.append(zufaelligekarte[i] // 13)

    return farbe



def zufallfuenf():
    zaehler=0
    zufuenf=[]
    randomKarten =karten
    random.shuffle(randomKarten)
    while zaehler < 5 :
        zufuenf.append(randomKarten[zaehler])
        zaehler = zaehler+1
    return zufuenf



def kombinationen(randomKarten):
    thisdic={}
    for i in range (0,len(randomKarten)):
        thisdic.update({randomKarten[i]: randomKarten.count(randomKarten[i])})
    
    return thisdic

def paar(random_karten):
    if 2 in kombinationen(zahlen(random_karten)).values():
        return (True)

def drilling(random_karten):
    if 3 in kombinationen(zahlen(random_karten)).values():
        return (True)

def full_house(random_karten):
    if 3 in kombinationen(zahlen(random_karten)).values() and 2 in kombinationen(zahlen(random_karten)).values():
        return (True)

def vierling(random_karten):
    if 4 in kombinationen(zahlen(random_karten)).values():
        return (True)

def flush(random_karten):
    if 5 in kombinationen(farbe(random_karten)).values():
        return (True)        


def straße(random_karten):
    sorted_karten = sorted(zahlen(random_karten))
    counter = 0
    for i in range(4):
        if sorted_karten[i] + 1 == sorted_karten[i + 1]:
            counter = counter + 1

    if counter == 4:
        return (True)


def straight_flush(random_karten):
    sorted_karten = sorted(zahlen(random_karten))
    counter = 0
    for i in range(4):
        if sorted_karten[i] + 1 == sorted_karten[i + 1]:
            counter = counter + 1

    if counter == 4 and 5 in kombinationen(farbe(random_karten)).values():
        return (True)

dic = {
    "paar" : 0,
    "drillinge" : 0,
    "straße" : 0,
    "flush" : 0,
    "full house" : 0,
    "vierer paar" : 0,
    "straight flush" : 0,
    }

for i in range(0,100000):
    randomKarte = zufallfuenf()

    if(straight_flush(randomKarte)):
        dic["straight flush"] = dic["straight flush"]+1
    elif(vierling(randomKarte)):
        dic["vierer paar"] = dic["vierer paar"]+1
    elif(full_house(randomKarte)):
        dic["full house"] = dic["full house"]+1
    elif(flush(randomKarte)):
        dic["flush"] = dic["flush"]+1
    elif(straße(randomKarte)):
        dic["straße"] = dic["straße"]+1
    elif(drilling(randomKarte)):
        dic["drillinge"] = dic["drillinge"]+1
    elif(paar(randomKarte)):
        dic["paar"] = dic["paar"]+1


if __name__ == "__main__":
    for i in dic:
        dic[i]= round(dic[i]/100000*100,3)
    print(dic)
