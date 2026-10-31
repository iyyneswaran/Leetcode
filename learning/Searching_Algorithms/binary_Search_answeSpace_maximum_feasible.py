def integer_sqrt(n: int) -> int:
    left = 0
    right = n

    while left < right:
        mid = (left + right + 1) // 2

        if mid * mid <= n:
            left = mid
        else:
            right = mid - 1

    return left