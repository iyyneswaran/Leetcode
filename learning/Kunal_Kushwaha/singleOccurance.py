# Except single value others are pairs [pairs => same value occuring two times]. Return the unique value.
def ans(arr):
    unique = 0
    for i in arr:
        unique ^= i

    return unique

arr = list(map(int, input().split()))
print(ans(arr))