import random

#Node Klasse für jedes Element in doppelt verketteten Liste
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

#doppelt verkettete Liste
class DoublyLinkedList:
    def __init__(self):
        #leere Liste
        self.arr = []
        #anfang und ende Liste
        self.head = None
        self.tail = None

    #fügt neues Element am ende der Liste hinzu
    def append(self, data):
        #neues node für übergebene data
        new_node = Node(data)
        #überprüft ob übergebene data integer
        if not isinstance(data, int):
            raise ValueError("Data must be an integer")
        #wenn liste leer, setzt head und tail für neue node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.arr.append(new_node)
        # Wenn Liste nicht leer, setzt Node des Tails auf neue Node,
        # setzt vorherigen Node auf den alten Tail und aktualisiert neuen Tail auf die neue Node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.arr.append(new_node)

#gibt länge zurück
    def length(self):
        return len(self.arr)
#gibt alle elemente aus
    def print_all_elements(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
#gibt node an der position an
    def get_node_at_index(self, index):
        #überprüft, ob index gültig
        if index < 0 or index >= len(self.arr):
            raise IndexError("Index out of range")
        #gibt node an angegebener Position zurück
        return self.arr[index]

#fügt ein neues element an angegebener Position in Liste ein
    def insert(self, index, data):
        #Überprüfe, ob das übergebene data ein integer ist
        if not isinstance(data, int):
            raise ValueError("Data must be an integer")
        #erstellt neues node für data
        new_node = Node(data)
        #wenn der angegebene index das letzte element der Liste ist, ruft append auf
        if index == len(self.arr):
            self.append(data)
        #sonst ruft node an gewünsch. pos. auf, setzt vorherige node 
        else:
            node_at_index = self.get_node_at_index(index)
            if node_at_index.prev:
                node_at_index.prev.next = new_node
            else:
                self.head = new_node
            new_node.prev = node_at_index.prev
            new_node.next = node_at_index
            node_at_index.prev = new_node
            self.arr.insert(index, new_node)

#entfernt element an angegebener Position in Liste
    def remove(self, index):
        #in range?
        if index < 0 or index >= len(self.arr):
            raise IndexError("Index out of range")
        node_to_remove = self.get_node_at_index(index)
        if node_to_remove.prev:
            node_to_remove.prev.next = node_to_remove.next
        else:
            self.head = node_to_remove.next
        if node_to_remove.next:
            node_to_remove.next.prev = node_to_remove.prev
        else:
            self.tail = node_to_remove.prev
        self.arr.pop(index)

def main():
    #erstellt doublylinkedlist mit 10 elemente und gibt länge aus
    #druckt elemente aus
    dllist = DoublyLinkedList()
    for i in range(10):
        dllist.append(random.randint(1, 100))
    print("Length of the list:", dllist.length())
    dllist.print_all_elements()
    #fügt element an pos. 3 ein und gibt länge wieder aus
    dllist.insert(3, 50)
    print("Length of the list after insert:", dllist.length())
    dllist.print_all_elements()
    #entfernt element an pos. 5
    #druckt nochmals aus
    dllist.remove(5)
    print("Length of the list after remove:", dllist.length())
    dllist.print_all_elements()

if __name__ == "__main__":
    main()
