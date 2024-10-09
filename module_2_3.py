my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_index = 0

while list_index < len(my_list):
    print(my_list[list_index])
    list_index = list_index + 1
    if my_list[list_index] == 0:
        list_index = list_index + 1
    elif my_list[list_index] < 0:
        break












