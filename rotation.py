def left_rotate(arr, d):def left_rotate(arr = d % len(arr)
    return arr[d:] + arr[:d]

def right_rotate(arr, d):
    d = d % len(arr)
    return arr[-d:] + arr[:-d]

def reverse_array(arr):
    return arr[::-1]
