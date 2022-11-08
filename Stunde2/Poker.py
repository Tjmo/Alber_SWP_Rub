import random
#deck erstellen ------------------------------------------------------------
# 11 = J, 12 = Q, 13 = K, 14 = A
karten_werte = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
farben = ["kreuz", "karo", "herz", "pik"]
 
gesichter_karten = { #dictionary für alles über 10
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
    11: "J",
    12: "Q",
    13: "K",
    14: "A"
}
class Karte:
    def __init__(eigene, wert, farbe):
        eigene.wert = wert
        eigene.farbe = farbe

def generiere_karten():
    karten = [] #leere Liste von Karten
    for wert in karten_werte:
        for farbe in farben: #doppelte for-schleife damit Karten Farbe und Werte zugewiesen bekommen
            if wert in gesichter_karten:
                _karte = Karte(gesichter_karten[wert], farbe)#wenn karte Gesicht hat, speichern als gesicht
            else:
                _karte = Karte(wert, farbe)#sonst den normalen wert der karte
            karten.append(_karte) #fügen Karte den generierten Karten hinzu
    return karten #geben Karte zurück
 
karten = generiere_karten()#karten generiert

#karten geben ------------------------------------------------------------

def karte_ausgeben(karten):
    i = random.randint(0, len(karten)-1) #zufällige Karte bekommen aus unserem deck
    karte = karten[i] #Karte bekommt gewisse Wertigkeit durch i
    karten.pop(i) #Karte wird entfernt vom Stapel
    return karte, karten #Entfernte Karte vom Stapel wird zurück gegeben

def ausgeben(karten = karten):
    karte1, karten = karte_ausgeben(karten) #Erste Karte wird aus dem Deck ausgegeben
    karte2, karten = karte_ausgeben(karten) #Zweite Karte wird aus dem Deck ausgegeben
    deine_hand = [karte1, karte2] #mein Deck aus diesen 2 Karten
    return deine_hand
 

deine_hand = ausgeben()
print([(karte.wert, karte.farbe) for karte in deine_hand]) #die Werte und Farben der Karten in meiner Hand werden ausgegeben


#karten geben ------------------------------------------------------------
def ersten3(karten=karten): #ersten 3 karten werden gegeben
    karte1, karten = karte_ausgeben(karten)
    karte2, karten = karte_ausgeben(karten)
    karte3, karten = karte_ausgeben(karten)
    return [karte1, karte2, karte3] #gibt die ersten 3 aufgedeckten Karten wieder
 
def tisch_ausgeben(karten=karten): #gibt mir die Karten aus
    karte, karten = karte_ausgeben(karten)
    return karte
 
tisch = ersten3() #die ersten drei werden nun ausgegeben
tisch.append(tisch_ausgeben())
tisch.append(tisch_ausgeben()) #die 4. und 5. Karten wird nun aufgedeckt
print(f"Alle Karten aufgedeckt: {[(karte.wert, karte.farbe) for karte in tisch]}")

#nimmt meine karten und die auf dem Tisch, um herauszufinden welche kombination die höchste wäre
def ermitteln(hand, tisch):
    total_hand = hand + tisch #alle 7 Karten
    # zählt werte und farbe
    zahlen = {} #für Paare und Dreier
    farben = {} #---||---
    werts = set() #straße oder nicht
    # geht alle Karten durch
    for karte in total_hand:
        if karte.wert in gesichter_karten:
            karten_wert = gesichter_karten[karte.wert] #wenn karte höher 10 dann soll sie ihren wert erhalten
        else:
            karten_wert = karte.wert #sonst bleibt alles gleich
        werts.add(karten_wert)
        if karten_wert in zahlen:
            zahlen[karten_wert] += 1
        else:
            zahlen[karten_wert] = 1
        if karte.farbe in farben:
            farben[karte.farbe] += 1
        else:
            farben[karte.farbe] = 1

# was hab ich in der hand ------------------------------------------------------
  # sortiert zahlen und farben
    sortierte_zahlen = sorted(zahlen.items(), key=lambda item:(item[1], item[0]), reverse=True)
    sortierte_farben = sorted(farben.items(), key=lambda item:(item[1], item[0]), reverse=True)
 
    # checkt ob werts ein straße beinhaltet
    run = [sorted(list(werts))[0]]
    lastval = sorted(list(werts))[0]
    is_straße = False
    for val in sorted(list(werts)):
        if val - lastval == 1:
            run.append(val)
        else:
            run = [val]
        lastval = val
        if len(run) == 5:
            is_straße = True
            break
    # checkt ob sortierte_farben ein flush beinhaltet
    is_flush = False
    if sortierte_farben[0][1] == 5:
        is_flush = True

#höchste hand -------------------------------------------------------------------

 # checkt für straight flush
    if is_straße:
        if is_flush:
            return "Straight Flush!"
    if sortierte_zahlen[0][1] == 4: #zahlen 4 gleich (durch zähler) dann quad
        return f"Quad {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}s!"
    if sortierte_zahlen[0][1] == 3: #zahlen 3 gleich und 2 gleich full house
        if sortierte_zahlen[1][1] == 2:
            return f"Full house {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}s over {gesichter_karten.get(sortierte_zahlen[1][0]) if sortierte_zahlen[1][0] in gesichter_karten else sortierte_zahlen[1][0]}s!"
    if is_flush:
        return f"Flush in {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}!"
    if is_straße:
        return f"Straße! {run}"
    # checkt für Gruppen
       
    if sortierte_zahlen[0][1] == 3:
        return f"Triple {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}s!"
    if sortierte_zahlen[0][1] == 2:
        if sortierte_zahlen[1][1] == 2:
            return f"Zwei Paare {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]} and {gesichter_karten.get(sortierte_zahlen[1][0]) if sortierte_zahlen[1][0] in gesichter_karten else sortierte_zahlen[1][0]}!"
        else:
            return f"Paare mit {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}!"
    if sortierte_zahlen[0][1] == 1:
        return f"Hohe Karte {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}!"

def ermitteln(hand, tisch):
    total_hand = hand + tisch
    # zählt werte und farbe
    zahlen = {}
    farben = {}
    werts = set()
    # schleife durch alle karten
    for karte in total_hand:
        if karte.wert in gesichter_karten:
            karten_wert = gesichter_karten[karte.wert]#wenn gesicht dann wert zugewiesen
        else:
            karten_wert = karte.wert
        werts.add(karten_wert)
        if karten_wert in zahlen:
            zahlen[karten_wert] += 1
        else:
            zahlen[karten_wert] = 1
        if karte.farbe in farben:
            farben[karte.farbe] += 1
        else:
            farben[karte.farbe] = 1
    # ordnet zahlen und farben
    sortierte_zahlen = sorted(zahlen.items(), key=lambda item:(item[1], item[0]), reverse=True)
    sortierte_farben = sorted(farben.items(), key=lambda item:(item[1], item[0]), reverse=True)
 
    # checkt ob werts eine straße enthält
    run = [sorted(list(werts))[0]]
    lastval = sorted(list(werts))[0]
    is_straße = False
    for val in sorted(list(werts)):
        if val - lastval == 1:
            run.append(val)
        else:
            run = [val]
        lastval = val
        if len(run) == 5:
            is_straße = True
            break
   
    # checkt ob sortierte_farben ein flush enthält
    is_flush = False
    if sortierte_farben[0][1] == 5:
        is_flush = True
    # checkt ob straight flush
    if is_straße:
        if is_flush:
            return "Straight Flush!"
    if sortierte_zahlen[0][1] == 4: #checkt ob viererpaarl
        return f"Quad {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}s!"
    if sortierte_zahlen[0][1] == 3: #checkt ob 3er und 2er paar da ist (full house)
        if sortierte_zahlen[1][1] == 2:
            return f"Full house {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}s over {gesichter_karten.get(sortierte_zahlen[1][0]) if sortierte_zahlen[1][0] in gesichter_karten else sortierte_zahlen[1][0]}s!"
    if is_flush:
        return f"Flush in {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}!"
    if is_straße:
        return f"Straße! {run}"
    # check for groups
       
    if sortierte_zahlen[0][1] == 3:
        return f"Triple {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}s!"
    if sortierte_zahlen[0][1] == 2:
        if sortierte_zahlen[1][1] == 2:
            return f"Zwei Paare {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]} and {gesichter_karten.get(sortierte_zahlen[1][0]) if sortierte_zahlen[1][0] in gesichter_karten else sortierte_zahlen[1][0]}!"
        else:
            return f"Paar mit {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}!"
    if sortierte_zahlen[0][1] == 1:
        return f"Hohe Karte {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}!"


def festlegen(hand, tisch):#gibt aus, was die beste Kombination aus deiner Hand und dem was auf dem Tisch liegt wäre
    print(f"Deine beste Kombination wäre: {ermitteln(hand, tisch)}")
 
festlegen(deine_hand, tisch)


