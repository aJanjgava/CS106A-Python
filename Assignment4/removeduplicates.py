"""
This program gives you practice with constructing a new list
based on values given to you by the user.  You also get
practice removing duplicates from that list
"""


def read_list():
    """
    This function should ask the user for a series of integer values
    (until the user enters 0 to stop) and store all those values in a
    list.  That list should then be returned by this function.
    """
    user_list = []
    while True:
        ask_for_numbers = int(input('Enter value (0 to stop): '))
        user_list.append(ask_for_numbers)
        if ask_for_numbers == 0:
            break
    user_list.pop()
    return user_list


def remove_duplicates(num_list):
    """
    This function is passed a list of integers and returns a new
    list with all duplicate values from the original list remove.
    # >>> remove_duplicates([1, 2, 3, 2, 3, 4])
    [1, 2, 3, 4]
    # >>> remove_duplicates([1, 1, 1])
    [1]
    # >>> remove_duplicates([])
    []
    """
    new_list = []
    for elem in num_list:
        if elem not in new_list:
            new_list.append(elem)
    return new_list


def main():
    num_list = read_list()
    print("Original list entered by user: ")
    print(num_list)

    no_duplicates = remove_duplicates(num_list)
    print("List with duplicates removed: ")
    print(no_duplicates)


if __name__ == '__main__':
    main()
