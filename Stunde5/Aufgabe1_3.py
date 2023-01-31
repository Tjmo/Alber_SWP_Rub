import random

#samsin hat Konstruktor, speichert in data und initialisiert next mit None
class samsin:
    def __init__(self, data):
        self.data = data
        self.next = None

#LinkedList hat Konstruktor und initialisiert head mit None
#Methoden in klasse sind für die Verwaltung der Liste
class LinkedList:
    def __init__(self):
        self.head = None
        
    #fügt neues Element an Ende der Liste
    #(erstellt samsinobjekt und verkettet an ende der Liste)
    #überprüft ebenfalls ob daten ganzzahlig (int) -> sonst ValueError
    def append(self, data):
        if not isinstance(data, int):
            raise ValueError("Muss int sein")
        new_samsin = samsin(data)
        if self.head is None:
            self.head = new_samsin
            return
        last_samsin = self.head
        while last_samsin.next:
            last_samsin = last_samsin.next
        last_samsin.next = new_samsin
        

    #druckt alle Datenelemente aus
    def print_list(self):
        curr_samsin = self.head
        while curr_samsin:
            print(curr_samsin.data)
            curr_samsin = curr_samsin.next

    #berechnet Länge durch durchlaufen und durch Zähler(count) erhöhen
    def length(self):
        curr_samsin = self.head
        count = 0
        while curr_samsin:
            count += 1
            curr_samsin = curr_samsin.next
        return count
    
    #druckt alle Elemente aus
    def print_all_elements(self):
        curr_samsin = self.head
        while curr_samsin:
            print(curr_samsin.data)
            curr_samsin = curr_samsin.next

#erstellt Instanz der Klasse LInkedList und fügt 10 zuf.
#   int-werte (1-100) hinzu, gibt Länge d. Liste aus und druckt Elemente aus
def main():
    llist = LinkedList()
    for o in range(10):
        llist.append(random.randint(1,100))
    print("Length of linked list:",llist.length())
    llist.print_all_elements()

#sorgt dafür, dass Programm nur ausgeführt wird, wenn Programm direkt ausgeführt wird (nicht importiert) und nicht wenn es als modul importiert wird
if __name__ == "__main__":
    main()