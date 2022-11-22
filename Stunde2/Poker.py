import numpy as np
import random

global __karten
__karten = []

for i in range(52): # 52 Ziffern da 13Karten * 4Farben | danach befüllen wir Liste karten mit den zahlen
    __karten.append(i)


def zahlen(random_karten): #werteliste, wir nehmen 5 karten und befüllen diese mit den zugehörigen werten (1-13% gibt max 13)
    werte = []
    for i in range(5):
        werte.append(random_karten[i] % 13)
    return werte


def farbe(zufaelligekarte): #farbliste, wir nehmen 5 karten und befüllen diese mit den zugehörigen farben (0-12// gibt alle 13 zahlen eine höhere zahl 0,1,2,3)
    farbe = []
    for i in range(5):
        farbe.append(zufaelligekarte[i] // 13)
    return farbe


def zufallfuenf(): # fünf zufällige karten werden ausgegeben
    zaehler=0
    zufuenf=[]
    randomKarten =__karten
    random.shuffle(randomKarten)
    while zaehler < 5 :
        zufuenf.append(randomKarten[zaehler])
        zaehler = zaehler+1
    return zufuenf


def kombinationen(randomKarten): #speichern die Karten in einem Dictionary
    thisdic={}
    for i in range (0,len(randomKarten)):
        thisdic.update({randomKarten[i]: randomKarten.count(randomKarten[i])})
    return thisdic


def paar(random_karten): #wenn 2er kombinationen return true
    if 2 in kombinationen(zahlen(random_karten)).values():
        return (True)

def drilling(random_karten): #wenn 3er kombinationen return true
    if 3 in kombinationen(zahlen(random_karten)).values():
        return (True)

def full_house(random_karten):#wenn 2er und 3er kombinationen return true
    if 3 in kombinationen(zahlen(random_karten)).values() and 2 in kombinationen(zahlen(random_karten)).values():
        return (True)

def vierling(random_karten): #wenn 4er kombinationen return true
    if 4 in kombinationen(zahlen(random_karten)).values():
        return (True)

def flush(random_karten): #wenn 5er farbkombinationen return true
    if 5 in kombinationen(farbe(random_karten)).values():
        return (True)

def straße(random_karten): #wenn die sortierten karten in steigender reihenfolge um immer 1 zunehmen return true
    sorted_karten = sorted(zahlen(random_karten))
    counter = 0
    for i in range(4):
        if sorted_karten[i] + 1 == sorted_karten[i + 1]:
            counter = counter + 1
    if counter == 4:
        return (True)

def straight_flush(random_karten): #wenn alle 5 in Kombinationen und Karten steigern
    sorted_karten = sorted(zahlen(random_karten))
    counter = 0
    for i in range(4):
        if sorted_karten[i] + 1 == sorted_karten[i + 1]:
            counter = counter + 1

    if counter == 4 and 5 in kombinationen(farbe(random_karten)).values():
        return (True)


dic = { #kombinationen zum zählen
    "paar" : 0,
    "drillinge" : 0,
    "straße" : 0,
    "flush" : 0,
    "full house" : 0,
    "vierer paar" : 0,
    "straight flush" : 0,
    }

for i in range(0,100000): #wir führen es 100000 mal aus und jedesmal wenn eine kombination hat, dic counter +1
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

def main():
    for i in dic:
        dic[i]= round(dic[i]/100000*100,3)
    print(dic)
    
if __name__ == "__main__":
    main()
