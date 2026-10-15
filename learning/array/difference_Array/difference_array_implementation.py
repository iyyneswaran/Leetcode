
def apply_range_additions(n, updates):
    diff = [0] * (n + 1)

    # Record each update at its boundaries.
    for left, right, value in updates:
        diff[left] += value
        diff[right + 1] -= value

    # Reconstruct the final array using prefix sums.
    result = [0] * n
    running = 0

    for i in range(n):
        running += diff[i]
        result[i] = running

    return result


updates = [
    (1, 3, 3),
    (2, 4, 2)
]

print(apply_range_additions(5, updates))
# [0, 3, 5, 5, 2]