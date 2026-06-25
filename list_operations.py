def swap_first_last(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

def list_sum(lst):
    return sum(lst)

def list_multiply(lst):
    result = 1
    for i in lst:
        result *= i
    return result

def remove_negatives(lst):
    return [i for i in lst if i >= 0]
