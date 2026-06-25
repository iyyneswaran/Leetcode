def rangeSum(sumValue, num1, num2):
    if num1 > num2:
        return sumValue
    else:
        return num1 + rangeSum(sum, num1 + 1, num2)

num1, num2 = map(int, input().split())
sumValue = 0
print(rangeSum(sumValue, num1, num2))