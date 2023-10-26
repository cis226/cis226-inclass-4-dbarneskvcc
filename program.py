"""Program code"""

from datastructures import LinkedList
from employee import Employee


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

    # Remove from front
    linkedlist.remove_from_front()
    linkedlist.remove_from_front()
    linkedlist.remove_from_front()

    # Print out the list
    linkedlist.display()

    # Remove fro back
    linkedlist.remove_from_back()
    linkedlist.remove_from_back()

    # Also have ability to get the value that was removed
    returned_number = linkedlist.remove_from_back()

    # Print out the returned number
    print(f"The removed value is: {returned_number}")

    # Can also use to store objects.
    employee_list = LinkedList()
    employee_list.add_to_front(Employee("David", "Barnes", 750.00))
    employee_list.add_to_front(Employee("Jean-Luc", "Picard", 640.00))
    employee_list.display()
