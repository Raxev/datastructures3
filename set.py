class Set:
    """    
    Set Python List Implementation
    """
    def __init__(self):
        """
        Creates an empty set
        """
        self._items = list()

    def __len__(self):
        """
        Returns the number of items in the set
        """
        return len(self._items)

    def __contains__(self, item):
        """
        Returns True if the set contains the passed in item
        and False, otherwise
        """
        return item in self._items

    def add(self, item):
        """
        Adds a new item to the set, 
        if the item is not already in the set
        """
        if item not in self._items:
            self._items.append(item)

    def remove(self, item):
        """
        Removes an item from the set, if it exists in the set
        """
        if item in self._items:
            self._items.remove(item)

    def __str__(self):
        """
        Returns a string representation of the set
        """
        return str(self._items)

    def __eq__(self, other_set):
        """
        Returns True if all the items in this set are the same
        items in the passed in other_set, and False, otherwise
        """
        if len(self) != len(other_set):
            return False
        else:
            return self.isSubsetOf(other_set)

    def isSubsetOf(self, other_set):
        """
        Returns True if all the items in this set are also 
        in the passed in other_set, and False, otherwise
        """
        for item in self:
            if item not in other_set:
                return False
        return True

    def union(self, other_set):
        """
        Creates a new set by combining the items in this set 
        with the items in the passed in other_set
        """
        new_set = Set()
        new_set._items.extend(self._items)
        for item in other_set:
            if item not in self:
                new_set._items.append(item)
        return new_set

    def intersection(self, other_set):
        """
        Creates a new set consisting of the items that are
        in both this set and in the passed in other_set
        """
        new_set = Set()
        for item in self:
            if item in other_set:
                new_set._items.append(item)
        return new_set

    def difference(self, other_set):
        """
        Creates a new set consisting of the items that are
        in this set, but not in the passed in other_set
        """
        new_set = Set()
        for item in self:
            if item not in other_set:
                new_set._items.append(item)
        return new_set
        
    def __iter__(self):
        """
        Creates a new set consisting of the items that are
        in this set, but not in the passed in other_set
        """
        return SetIterator(self._items)
        

class SetIterator:
    """
    An iterator for the Set ADT implemented as a Python list.
    """
    def __init__(self, the_list):
        """
        Initialize the list, from the one passed in
        Set the current item to index 0
        """
        self._set_items = the_list
        self._cur_item = 0

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
        if self._cur_item < len(self._set_items):
            item = self._set_items[self._cur_item]
            self._cur_item += 1
            return item
        else:
            raise StopIteration
