"""Program code"""

from datastructures import LinkedList


def main(*args):
    """Method to run program"""
    # Make instance of Linked List
    linkedlist = LinkedList()

    # Add to the front and back a few times
    linkedlist.add_to_front(5)
    linkedlist.add_to_front(4)
    linkedlist.add_to_front(3)
    linkedlist.add_to_back(6)
    linkedlist.add_to_back(7)
    linkedlist.add_to_back(8)

    # Print out the list
    linkedlist.display()
