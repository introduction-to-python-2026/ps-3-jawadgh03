def move(my_list, direction):
    index_of_one = my_list.index(1)
    if direction == 'right':
        if index_of_one == len(my_list) - 1:
            return my_list
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1
    elif direction == 'left':
        if index_of_one == 0:
            return my_list
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1
    return my_list


def approximate_pi(n):
    pi_estimate = 0
    for i in range(n):
        term = ((-1) ** i) / (2 * i + 1)
        pi_estimate += term
    return 4 * pi_estimate
