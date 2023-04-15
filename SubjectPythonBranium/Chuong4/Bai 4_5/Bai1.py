import math


def input_convert_to_dict():
    # This function get information from keyboard push into dicts and return list include dicts
    str_number_dicts = input("Enter the number of test sets: ")
    number_dicts = int(str_number_dicts)
    dict_sets = []
    for i in range(number_dicts):
        str_number_pair = input("Enter the number pair: ")
        number_pair = int(str_number_pair)
        dict_i = dict()
        for j in range(number_pair):
            infor = input(f"Enter infor pair {j}: ").split()
            dict_i[infor[0]] = round(float(infor[1]), 2)
        dict_sets.append(dict_i)

    return dict_sets


def output(dict_sets: list):
    # This function show gpa of id student or show None if not found
    len_dict_sets = len(dict_sets)
    for i in range(len_dict_sets):
        list_id = input(f"Enter id if you want find in test {i}: ").split()
        len_list_id = len(list_id)
        for j in range(len_list_id):
            print(dict_sets[i].get(list_id[j]), end=' ')


output(input_convert_to_dict())