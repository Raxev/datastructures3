class HuffPQ:
    """
    The Huffman Priority Queue is implemented with a
    minimum heap that uses a Python list to store 
    the HuffTrees in a complete binary tree
    """ 
    def __init__(self):
        """
        Create an empty priority queue from a Python list
        """
        self._pq = []
        
    def __len__(self):
        """
        Return the number of elements in the queue
        """
        return len(self._pq)
        
    def _heapify(self, index):
        """
        Restore the Min Heap order starting 
        with the tree at the given index
        """
        left_index = self._get_left_child(index)
        right_index = self._get_right_child(index)
        smallest = index

        if (left_index < len(self)) and \
                self._pq[left_index].compare(self._pq[index]) < 0:
            smallest = left_index

        if (right_index < len(self)) and \
                self._pq[right_index].compare(self._pq[smallest]) < 0:
            smallest = right_index

        if smallest != index:
            temp = self._pq[index]
            self._pq[index] = self._pq[smallest]
            self._pq[smallest] = temp

            self._heapify(smallest)
                
    def _get_parent(self, index):
        """
        Return the parent index of the tree at the given index
        """
        return (index - 1) // 2

    def _get_left_child(self, index):
        """
        Return the left child index of the tree at the given index
        """
        return 2 * index + 1

    def _get_right_child(self, index):
        """
        Return the right child index of the tree at the given index
        """
        return 2 * index + 2

    def dequeue(self):
        """
        Remove the root tree which has the minimum value
        """
        if len(self) == 0:
            return None

        if len(self) == 1:
            root = self._pq[0]
            self._pq = []
            return root

        root = self._pq[0]
        self._pq[0] = self._pq[len(self) - 1]
        del self._pq[len(self) - 1]

        self._heapify(0)
        return root

    def enqueue(self, tree):
        """
        Inserts a new tree into the min heap at the bottom
        Then restore the heap order
        """
        self._pq.append(tree)
        index = len(self) - 1

        """
        Swap the element at the given index with its parent
        until the parent is smaller than that element 
        """
        while (index != 0) and \
                (self._pq[self._get_parent(index)].compare(self._pq[index]) > 0):

            temp = self._pq[index]
            self._pq[index] = self._pq[self._get_parent(index)]
            self._pq[self._get_parent(index)] = temp

            index = self._get_parent(index)

    def peek(self):
        """
        Returns the tree with minimum value (root tree)
        """
        return self._pq[0]
