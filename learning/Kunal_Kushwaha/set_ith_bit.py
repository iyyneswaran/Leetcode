def set_ith_bit(number, position):
    return number | (1 << position)

print(set_ith_bit(int(input()), int(input())))