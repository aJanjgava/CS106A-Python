"""
This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""

INPUT_FILE = 'bill1.txt'


def main():
    """
    Add your code (remember to delete the "pass" below)
    """
    result_dict = format_bill(INPUT_FILE)
    total_expenditure(result_dict)


def format_bill(bill):
    dict_bill = {}
    file = open(bill)
    for line in file:
        line = line[:-1]
        line = line.replace('$', '')
        line = line.replace('[', '')
        line = line.replace(']', '')
        line = line.split()
        line = line[1:]

        if len(line) == 3:
            pt1 = line[0] + ' ' + line[1]
            pt2 = line[2]
        elif len(line) > 3:
            pt1 = line[0] + ' ' + line[1] + ' ' + line[2]
            pt2 = line[3]
        else:
            pt1 = line[0]
            pt2 = line[1]

        if pt1 not in dict_bill:
            dict_bill[pt1] = [int(pt2)]
        else:
            dict_bill[pt1].append(int(pt2))

    return dict_bill


def total_expenditure(dictionary):
    for k in dictionary:
        total = sum(dictionary[k])
        print(f'{k}: ${total}')


if __name__ == '__main__':
    main()
