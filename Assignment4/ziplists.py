"""
This program gives you practice working with a list of lists.
"""


def zip2lists(list1, list2):
    """
    This function is passed two lists of strings.  Both lists both have
    the same length.  The function returns a new list that "zips" together
    the two lists passed in into a list that contains lists that are pairs of
    elements, one from each of the original lists, in order.  For example, if
    this function were passed the lists ['a', 'b', 'c'] and ['d', 'e', 'f'] it
    would return the list of lists:
    [['a', 'd'], ['b', 'e'], ['c', 'f']]
    The original lists passed in should not be changed.
    Note that if this function is passed two empty lists, it should just
    return an empty list, since there would be no lists (of pairs) in the
    result.
    # >>> zip2lists(['a', 'b', 'c'], ['d', 'e', 'f'])
    [['a', 'd'], ['b', 'e'], ['c', 'f']]
    # >>> zip2lists(['one'], ['two'])
    [['one', 'two']]
    # >>> zip2lists([], [])
    []
    """
    new_list = []
    for i in range(len(list1)):
        add_list = []
        add_list.append(list1[i])
        add_list.append(list2[i])
        new_list.append(add_list)
    return new_list


def main():
    result_list = zip2lists(['a', 'b', 'c'], ['d', 'e', 'f'])
    print(result_list)  # should print [['a', 'd'], ['b', 'e'], ['c', 'f']]



if __name__ == '__main__':
    main()
