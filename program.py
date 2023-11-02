"""Program code"""

from datastructures import LinkedList, HashTable
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

    ###############################
    # Hash Table Work
    ###############################

    # Demonstrate how the hash table works
    valley_num_to_name = HashTable()
    print()
    print("Adding some entries to the Hashtable")
    print("EX: valley_num_to_name.put(12345, 'David Barnes')")

    valley_num_to_name.put(12345, "Jame Kirk")
    valley_num_to_name.put(23456, "Benjamin Sisko")
    valley_num_to_name.put(34567, "Kathryn Janeway")
    valley_num_to_name.put(45678, "Jean-Luc Picard")
    valley_num_to_name.put(56789, "Jonathan Archer")

    print("The created hash table")
    print(valley_num_to_name)
    print(valley_num_to_name.show_array())
    print("*****************************")

    print("Get a single value out from the hash table")
    print("valley_num_to_name.get(45678)")
    print(valley_num_to_name.get(45678))
    print()

    print("What if we add 2 entries that collide")
    print("valley_num_to_name.put(26189, 'First Entry')")
    valley_num_to_name.put(26189, "First Entry")
    print("valley_num_to_name.put(26092, 'Second Entry')")
    valley_num_to_name.put(26092, "Second Entry")

    print()
    print(valley_num_to_name)
    print(valley_num_to_name.show_array())
    print()

    print("Get the first entry out")
    print("valley_num_to_name.get(26189)")
    print(valley_num_to_name.get(26189))
    print("Got second entry instead. First was overwritten")
    print()
    print()

    # What about using string keys?
    print("What about using string keys?")
    string_hash_table = HashTable()
    string_hash_table.put("foobar", "Joe Smith")
    string_hash_table.put("barbaz", "Fred Drees")
    print(string_hash_table.get("foobar"))
    print(string_hash_table.get("barbaz"))
    print("String keys work too!")
    # String keys work thanks to the built-in hash function
    # being able to convert anything to an int hashed value.
