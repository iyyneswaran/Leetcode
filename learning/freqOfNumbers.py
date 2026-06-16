arr = [1,3, 5, 3, 1, 4, 6, 3, 5]
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)


# alternative 
for num in arr:
    freq[num] = freq.get(num, 0) + 1
    
    