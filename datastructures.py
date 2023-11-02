"""Data Structures"""
import os


class LinkedList:
    """Linked List Data Structure"""

    class Node:
        """Node in a data structure"""

        def __init__(self):
            """Constructor for Node"""
            self.data = None
            self.next = None

    def __init__(self):
        """Constructor for Linked List class"""
        self._head = None
        self._tail = None
        self._size = 0

    @property
    def is_empty(self):
        """Whether linked list is empty or not"""
        return self._head is None

    @property
    def size(self):
        """Property for size"""
        return self._size

    def add_to_front(self, data):
        """Add a new element to the front of the linked list"""
        # Make a new variable to also reference the head of the list
        old_head = self._head
        # Make a new node and assign it to the head var
        self._head = self.Node()
        # Set the data on the new Node
        self._head.data = data
        # Make the next property fo the new node point to the old node
        self._head.next = old_head
        # Increment size
        self._size += 1
        # Ensure that if we are adding the very first node to the linked list
        # that the tail will be pointing to the new node we create
        if self._size == 1:
            self._tail = self._head

    def add_to_back(self, data):
        """Add a new element to the back of the linked list"""
        # Make a pointer to the tail called old tail
        old_tail = self._tail
        # Make a new node and assign it to the tail variable
        self._tail = self.Node()
        # Assign the data and set the next pointer
        self._tail.data = data
        self._tail.next = None  # Should not need, but expressing intent

        # Check to see if the list is empty. If so, make the head point
        # to the same location as the tail. Else, make old tail next
        # point to the tail
        if self.is_empty:
            # Make head and tail the same since first node added.
            self._head = self._tail
        else:
            # Make old tails next point to the new tail
            old_tail.next = self._tail

        # Increment the size
        self._size += 1

    def remove_from_front(self):
        """Remove element from front of linked list and return that elements data"""
        # If the list is empty raise an error
        if self.is_empty:
            raise IndexError("Nothing to remove. List is empty.")
        # Get the data to return
        data = self._head.data
        # Move the head pointer to the next in the list
        self._head = self._head.next
        # Decrease the size
        self._size -= 1
        # Check to see if we just removed the last node from the list
        if self.is_empty:
            # If so, tail  needs to be set to None
            self._tail = None
        # Return the data from the removed node
        return data

    def remove_from_back(self):
        """Remove element from back of Linked LIst and return that elements data"""
        # If this list is empty raise an error
        if self.is_empty:
            raise IndexError("Nothing to remove. List is empty")
        # Get the data to return
        data = self._tail.data

        # Check to see if we are on the last node.
        # If so, we can just set the head and tail to None since we want
        # to remove the only remaining node in the list
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            # We need to traverse the list and stop right before we reach the tail.
            # Create a temporary node to use to "walk" down the list
            current = self._head
            # Keep moving forward until the current.next is equal to the tail.
            while current.next != self._tail:
                # Set the current pointer to the current pointer's next node.
                current = current.next
            # We are now in a postition to do some work.
            # Set the tail to the current postition
            self._tail = current
            # Make the last node that we are removing go away
            # by setting tail's next property to None
            self._tail.next = None
        # Return data
        return data

    def display(self):
        """Display the contents of the list via print"""
        print("This list is:")
        # Set up a current node to walk the list.
        # Start it at the head node.
        current = self._head
        # Loop through the nodes until we hit None,
        # which will signify the end of the list.
        while current is not None:
            print(current.data)
            # Move to the next node
            current = current.next
        print()


class HashTable:
    """Basic Hash Table data structure with no collision resolution"""

    PRIME_VALUE = 97

    def __init__(self):
        """Constructor"""
        self._values = [None for i in range(self.PRIME_VALUE)]
        # Keys not needed for functionality, but used so we can
        # see the keys when we print.
        self._keys = [None for i in range(self.PRIME_VALUE)]

    def put(self, key, value):
        """Put something into the hash table"""
        index_for_value = self._hash_function(key)
        self._values[index_for_value] = value
        self._keys[index_for_value] = key

    def get(self, key):
        """Get something out from the hash table"""
        index_for_value = self._hash_function(key)
        return self._values[index_for_value]

    def _hash_function(self, key):
        """Hash function used to has a key to an index"""
        try:
            hash_val = hash(key) % self.PRIME_VALUE
        except:
            hash_val = id(key) % self.PRIME_VALUE
        return hash_val

    def __str__(self):
        """String function"""
        return_string = f"Key   => Value{os.linesep}"
        return_string += f"--------------{os.linesep}"

        for i in range(self.PRIME_VALUE):
            if self._values[i] is not None:
                return_string += f"{self._keys[i]} => {self._values[i]}{os.linesep}"
        return return_string

    def show_array(self):
        """Show underlying array (list)"""
        return_string = f"Key   => Value{os.linesep}"
        return_string += f"--------------{os.linesep}"

        for i in range(self.PRIME_VALUE):
            value = ""
            if self._values[i] is not None:
                value = self._values[i]
            return_string += f"[{i}] => {value}{os.linesep}"
        return return_string
