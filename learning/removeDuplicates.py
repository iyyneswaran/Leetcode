arr = [1,3, 5, 3, 1, 4, 6, 3, 5]

result = []
seen = set()

for num in arr:
    if num not in seen:
        seen.add(num)
        result.append(num)

print(result)