def reset_nth_bit(number, position):
    mask = ~(1 << position)
    return number & mask

number = int(input())
position = int(input())
print(reset_nth_bit(number, position))