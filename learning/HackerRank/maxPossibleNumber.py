num = input().strip()
digits = list(map(int, input().split()))

num = list(num)
started = False

for i in range(len(num)):
    d = int(num[i])

    if not started:
        if digits[d] > d:
            num[i] = str(digits[d])
            started = True
    else:
        if digits[d] >= d:
            num[i] = str(digits[d])
        else:
            break

print("".join(num))