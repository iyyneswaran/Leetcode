def find_nth_bit(number, n):
    return (number >> n) & 1

print(find_nth_bit(int(input("Enter the number: ")), int(input("Enter the position: "))))

# one line
print((int(input()) >> int(input())) & 1)