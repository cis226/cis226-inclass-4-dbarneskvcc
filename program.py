"""Program code"""

from datastructures import LinkedList
from employee import Employee
from sorts import BubbleSort


def main(*args):
    """Method to run program"""

    ###########################
    # Linked List work
    ###########################

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

    ########################
    # Bubble Sort Work
    ########################
    # Demonstrate how the bubble sort works.
    bubble = BubbleSort()
    # Create list to sort
    list_to_sort = [4, 2, 7, 3, 8, 6, 1, 9, 5]
    # Sort the list
    bubble.sort(list_to_sort)
    # Loop and print values in list.
    for value in list_to_sort:
        print(value)

    # Do same with Employees
    emp_list = [
        Employee("D", "B", 750.00),
        Employee("J", "P", 550.00),
        Employee("F", "D", 250.00),
    ]
    # Sort the list
    bubble.sort(emp_list)
    # Loop and print values in list.
    for emp in emp_list:
        print(emp)
