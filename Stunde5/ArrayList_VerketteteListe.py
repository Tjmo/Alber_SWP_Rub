class ArrayList:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, value):
        self._data[index] = value
    
    def __delitem__(self, index):
        del self._data[index]
    
    def __iter__(self):
        return iter(self._data)
    
    def __contains__(self, value):
        return value in self._data
    
    def append(self, value):
        self._data.append(value)
    
    def insert(self, index, value):
        self._data.insert(index, value)
    
    def remove(self, value):
        self._data.remove(value)
    
    def pop(self, index=-1):
        return self._data.pop(index)
    
    def index(self, value, start=0, end=None):
        if end is None:
            end = len(self._data)
        return self._data.index(value, start, end)
    
    def count(self, value):
        return self._data.count(value)
    
    def clear(self):
        self._data.clear()


def main():
    # Erstellen einer neuen ArrayList
    my_list = ArrayList()

    # Elemente hinzufügen
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)

    # Ein Element einfügen
    my_list.insert(2, 5)

    # Ein Element entfernen
    my_list.remove(3)

    # Das letzte Element entfernen und zurückgeben
    popped_value = my_list.pop()
    print(f"Popped value: {popped_value}")

    # Index eines Elements finden
    index = my_list.index(2)
    print(f"Index of 2: {index}")

    # Anzahl der Vorkommen eines Elements zählen
    count = my_list.count(5)
    print(f"Count of 5: {count}")

    # ArrayList löschen
    my_list.clear()

    # Überprüfen, ob ein Element in der ArrayList enthalten ist
    x = 2
    print(f"Is {x} in my_list? {x in my_list}")


if __name__ == '__main__':
    main()