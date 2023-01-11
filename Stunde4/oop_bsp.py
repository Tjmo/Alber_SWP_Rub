from enum import Enum
# Firma
# ->Personen,mitarbeiter,gruppenleiter; in Abteilungen
# -->beide Geschlechter

# über Vererbung
# Firmenobjekt
# -> 

class Gender(Enum):
    Male = 0
    Female = 1

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    def print(self):
        return "Name: " + self.name + " Geschlecht: " + str(self.gender)
  

class Mitarbeiter(Person):
    def __init__(self, name, gender):
        super().__init__(name, gender)

    def print(self):
        return super().print()
    

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, gender):
        super().__init__(name, gender)
    
    def print(self):
        return super().print()

class Abteilung:
    def __init__(self, name, mitarbeiter, abteilungsleiter):
        self.name = name
        self.mitarbeiter = mitarbeiter
        self.abteilungsleiter = abteilungsleiter
    
    def print(self):
        return "Name: " + self.name +  " Abteilungsleiter: " + self.abteilungsleiter.print()

    def get_anz_mas(self):
        return len(self.mitarbeiter) + 1

    
class Firma:
    def __init__(self, name, kennung, abteilungen):
        self.name = name
        self.kennung = kennung
        self.abteilungen = abteilungen
    
    def get_anz_MAs(self):
        anz = 0
        for ab in self.abteilungen:
            anz += ab.get_anz_mas()
        return anz
    
    def get_abtl(self):
        abt = []
        for x in self.abteilungen:
            abt.append(x.abteilungsleiter)
        return abt
    
    def anz_F_M(self):
        dict_anz = {"Mann" : 0, "Frau" : 0, "Anz_Frau": 0}
        all_mit = []
        for x in self.abteilungen:
            all_mit = all_mit + x.mitarbeiter
            all_mit.append(x.abteilungsleiter)
        for i in all_mit:
            if(i.gender == Gender.Female):
                dict_anz["Frau"] +=1
            else:
                dict_anz["Mann"] += 1
        dict_anz["Anz_Frau (%)"] = round((dict_anz["Frau"]/self.get_anz_MAs())*100)
        return dict_anz
        

    def get_MAStaerke(self):
        biggest = 0
        name = ""
        for ab in self.abteilungen:
            if(ab.get_anz_MAs() > biggest):
                biggest = ab.get_anz_MAs()
                name = ab.name
        return name + "_" + str(biggest)

    def print(self):
        return self.name + "--" + str(self.kennung) + "--" + self.abteilungen



if __name__ == "__main__":
    mitarbeiter1 = [
        Mitarbeiter("Marcel", Gender.Male),
        Mitarbeiter("Paula", Gender.Female),
        
    ]
    mitarbeiter2 = [
        Mitarbeiter("Patrick", Gender.Male),
        Mitarbeiter("Timo", Gender.Male)
    ]

    abtl1 = Abteilungsleiter("Noah", Gender.Male)
    abtl2 = Abteilungsleiter("Maria", Gender.Female)

    x = Abteilung("Wirtschaft", mitarbeiter1, abtl1)
    y = Abteilung("Biomedi", mitarbeiter2, abtl2)

    firma = Firma("Programmers", 1337, [x, y])
    
    print("Anzahl Mitarbeiter", firma.get_anz_MAs())
    
    for x in firma.get_abtl():
        print("Abteilungsleiter", x.print())
    
    for x in firma.abteilungen:
        print("Abteilungen", x.print())
    
    #print("Größte Abteilung", firma.get_abtl())

    dict_anzh = firma.anz_F_M()
    print(dict_anzh)