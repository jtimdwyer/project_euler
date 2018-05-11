#this will combine two rows, where row_1 sits atop row_2
#returns a row to replace row_1

#the idea is that any path must at the last step choose teh larger of the
#two possible values. But this is equivalent to just increasing all of the
#second to last values by the prescribed amoutn and proceeding on the
#array with fewer rows. So I'm just taking those rows at the bottom, combining
#them, until we're left with only one row which contains the number we want.

def combine_two_rows(row_1, row_2):
    new_row = []
    for i, row_1_entry in enumerate(row_1):
        new_row.append(max(row_2[i], row_2[i+1]) + row_1_entry)
    return new_row

if __name__ == '__main__':
    with open('p18.txt') as file:
        array = []
        for line in file:
            new_line = [int(x) for x in line.split()]
            array.append(new_line)
    while len(array) > 1:
        row_2 = array.pop()
        row_1 = array.pop()
        new_row = combine_two_rows(row_1, row_2)
        array.append(new_row)
    print(array[0])
