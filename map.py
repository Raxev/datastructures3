from set import Set


class Map:
    """
    Python List Implementation for Map ADT
    """
    def __init__(self):
        """
        Creates an empty map
        """
        self._map_entries = list()

    def __len__(self):
        """
        Returns the number of entries in the map
        """
        return len(self._map_entries)

    def __contains__(self, key):
        """
        Returns True if the map contains the passed in key
        and False, otherwise
        """
        position = self._find_position(key)
        return position is not None

    def add(self, key, value):
        """
        Adds a new entry to the map if the passed in key 
        does not exist. Otherwise, the value replaces the 
        current value associated with the key.
        """
        position = self._find_position(key)
        if position is not None: 
            self._map_entries[position].value = value
            return False
        else: 
            entry = MapEntry(key, value)
            self._map_entries.append(entry)
            return True

    def get_value(self, key):
        """
        Returns the value associated with the passed in key,
        if the key is in the map
        """
        position = self._find_position(key)
        if position is not None: 
            return self._map_entries[position].value
        else:
            return None

    def remove(self, key):
        """
        Removes the entry associated with the passed in key.
        if the key is in the map
        """
        position = self._find_position(key)
        if position is not None: 
            return self._map_entries.pop(position)
        else:
            return None
            
    def __iter__(self):
        """
        Returns an iterator for traversing the keys in the map.
        """
        return MapIterator(self._map_entries)

    def get_entry_set(self):
        """
        Returns a set of each MapEntry object in the Map
        """
        entry_set = Set()
        for entry in self:
            entry_set.add(entry)
        return entry_set
        
    def get_key_set(self):
        """
        Returns a set of all the keys in Map
        """
        key_set = Set()
        for entry in self:
            key_set.add(entry.key)
        return key_set
        
    def get_value_set(self):
        """
        Returns a set of all the values in Map
        """
        value_set = Set()
        for entry in self:
            value_set.add(entry.value)
        return value_set
        
    def __str__(self):
        """
        Returns a string representation of each MapEntry
        """
        map_str = "{ "
        for entry in self:
            map_str += str(entry) + " "
        return map_str + "}"
    
    def _find_position(self, key):
        """
        Returns the position of a passed in key, or None, 
        if the key is not in the map
        """
        for pos in range(len(self)):
            if self._map_entries[pos].key == key:
                return pos
        return None


class MapEntry:
    """
    The class for holding the key/value pairs.
    """
    def __init__(self, key, value):
        """
        Creates a MapEntry with the passed in key/value pair
        """
        self.key = key
        self.value = value

    def __str__(self):
        """
        Returns a string version of the key and value
        """
        return str(self.key) + " : " + str(self.value)
        

class MapIterator:
    """
    An iterator for the Set ADT implemented as a Python list.
    """
    def __init__(self, the_map):
        """
        Initialize the list, from the one passed in
        Set the current item to index 0
        """
        self._map_entries = the_map
        self._cur_entry = 0

    def __iter__(self):
        """
        Return this iterator
        """
        return self

    def __next__(self):
        """
        Initialize the list, from the one passed in
        Set the current item to index 0
        """
        if self._cur_entry < len(self._map_entries):
            item = self._map_entries[self._cur_entry]
            self._cur_entry += 1
            return item
        else:
            raise StopIteration
