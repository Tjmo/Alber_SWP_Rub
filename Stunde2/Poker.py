import random
#deck erstellen ------------------------------------------------------------
# 11 = J, 12 = Q, 13 = K, 14 = A
karten_werte = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
farben = ["kreuz", "karo", "herz", "pik"]
 
gesichter_karten = {
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
    karten = []
    for wert in karten_werte:
        for farbe in farben:
            if wert in gesichter_karten:
                _karte = Karte(gesichter_karten[wert], farbe)
            else:
                _karte = Karte(wert, farbe)
            karten.append(_karte)
    return karten
 
karten = generiere_karten()

#karten geben ------------------------------------------------------------

def karte_ausgeben(karten):
    i = random.randint(0, len(karten)-1)
    karte = karten[i]
    karten.pop(i)
    return karte, karten

def ausgeben(karten = karten):
    karte1, karten = karte_ausgeben(karten)
    karte2, karten = karte_ausgeben(karten)
    deine_hand = [karte1, karte2]
    return deine_hand
 

deine_hand = ausgeben()
print([(karte.wert, karte.farbe) for karte in deine_hand])


#karten geben ------------------------------------------------------------
def ersten3(karten=karten): #ersten 3 karten werden gegeben
    karte1, karten = karte_ausgeben(karten)
    karte2, karten = karte_ausgeben(karten)
    karte3, karten = karte_ausgeben(karten)
    return [karte1, karte2, karte3]
 
def tisch_ausgeben(karten=karten): #gibt mir die Karten aus
    karte, karten = karte_ausgeben(karten)
    return karte
 
tisch = ersten3() #die 2 Folgenden werden danach aufgedeckt
tisch.append(tisch_ausgeben())
tisch.append(tisch_ausgeben())
print(f"Alle Karten aufgedeckt: {[(karte.wert, karte.farbe) for karte in tisch]}")

def ermitteln(hand, tisch):
    total_hand = hand + tisch #alle 7 Karten
    # zählt werte und farbe
    zahlen = {} #für Paare und Dreier
    farben = {} #---||---
    vals = set() #straight oder nicht
    # geht alle Karten durch
    for karte in total_hand:
        if karte.wert in gesichter_karten:
            karten_wert = gesichter_karten[karte.wert] #wenn karte höher 10 dann soll sie ihren wert erhalten
        else:
            karten_wert = karte.wert #sonst bleibt alles gleich
        vals.add(karten_wert)
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
 
    # checkt ob vals ein straight beinhaltet
    run = [sorted(list(vals))[0]]
    lastval = sorted(list(vals))[0]
    is_straight = False
    for val in sorted(list(vals)):
        if val - lastval == 1:
            run.append(val)
        else:
            run = [val]
        lastval = val
        if len(run) == 5:
            is_straight = True
            break
    # checkt ob sortierte_farben ein flush beinhaltet
    is_flush = False
    if sortierte_farben[0][1] == 5:
        is_flush = True

#höchste hand -------------------------------------------------------------------

 # check for straight flush
    if is_straight:
        if is_flush:
            return "Straight Flush!"
    if sortierte_zahlen[0][1] == 4: #zahlen 4 gleich (durch zähler) dann quad
        return f"Quad {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}s!"
    if sortierte_zahlen[0][1] == 3: #zahlen 3 gleich und 2 gleich full house
        if sortierte_zahlen[1][1] == 2:
            return f"Full house {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}s over {gesichter_karten.get(sortierte_zahlen[1][0]) if sortierte_zahlen[1][0] in gesichter_karten else sortierte_zahlen[1][0]}s!"
    if is_flush:
        return f"Flush in {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}!"
    if is_straight:
        return f"Straße! {run}"
    # check for groups
       
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
    vals = set()
    # schleife durch alle karten
    for karte in total_hand:
        if karte.wert in gesichter_karten:
            karten_wert = gesichter_karten[karte.wert]
        else:
            karten_wert = karte.wert
        vals.add(karten_wert)
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
 
    # checkt ob vals ein straight enthält
    run = [sorted(list(vals))[0]]
    lastval = sorted(list(vals))[0]
    is_straight = False
    for val in sorted(list(vals)):
        if val - lastval == 1:
            run.append(val)
        else:
            run = [val]
        lastval = val
        if len(run) == 5:
            is_straight = True
            break
   
    # checkt ob sortierte_farben ein flush enthält
    is_flush = False
    if sortierte_farben[0][1] == 5:
        is_flush = True
    # checkt ob straight flush
    if is_straight:
        if is_flush:
            return "Straight Flush!"
    if sortierte_zahlen[0][1] == 4:
        return f"Quad {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}s!"
    if sortierte_zahlen[0][1] == 3:
        if sortierte_zahlen[1][1] == 2:
            return f"Full house {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}s over {gesichter_karten.get(sortierte_zahlen[1][0]) if sortierte_zahlen[1][0] in gesichter_karten else sortierte_zahlen[1][0]}s!"
    if is_flush:
        return f"Flush in {gesichter_karten.get(sortierte_zahlen[0][0]) if sortierte_zahlen[0][0] in gesichter_karten else sortierte_zahlen[0][0]}!"
    if is_straight:
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



"""
nimmt dein Blatt und die Karten auf dem Tisch
ermittelt die werte
gibt den Sieger wieder mit allen Werten aufgewiesen
"""
def festlegen(hand, tisch):
    print(f"Deine höchste Poker Hand: {ermitteln(hand, tisch)}")
 
festlegen(deine_hand, tisch)


