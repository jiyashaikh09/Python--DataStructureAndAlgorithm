def is_armstrong(num):
    order = len(str(num))
    return sum(int(digit) ** order for digit in str(num)) == num

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n / 2)):
        if n % i == 0:
            return False
    return True
