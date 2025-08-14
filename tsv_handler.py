import csv

def read_from_tsv(file_name):
    with open(file_name + '.tsv', 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
        our_tsv_data = list(reader)
    return our_tsv_data

def write_to_tsv(file_name, data_to_write, mode,
                 headers=None):
    # Validate the headers parameter

    # This function "isinstance" checks whether "headers" is of type list
    # if it is, it will return True, therefore making it "if True"
    # otherwise, it will return False, making it "if False"
    # assert isinstance(headers, list)

    if (isinstance(headers, list) or headers is None) and isinstance(data_to_write, list):
        the_file = open(file_name + '.tsv', mode, encoding='utf-8', newline='')
        writer = csv.writer(the_file, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
        if headers is not None:
            writer.writerow(headers)
        writer.writerow(data_to_write)
        print("File is saved! Wohoo!")
        return True
    else:
        print("[Dad Jokes]: Headers should be a list or None. Please give headers as a list of elements")
        return False

# write_to_tsv(['id', 'joke'], 'jokes_told_database')


# Code below explains function scoping and pass by value vs pass by reference
# a = [10, 20, 30]
# c = 10
# def append_number_to_list(the_list, number_to_append):
#     the_list.append(number_to_append)
#
# def add_to_c(number_to_add):
#     c + number_to_add
#
# x = append_number_to_list(a, 40)
# z = add_to_c(20)
# print(x)
# print(a)
