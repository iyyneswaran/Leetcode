def can_ship(weights: list[int], capacity: int, days: int) -> bool:
    required_days = 1
    current_load = 0

    for weight in weights:
        if current_load > capacity:
            required_days += 1
            current_load = 0

        current_load += weight

    return required_days <= days

def ship_capacity(weights: list[int], days: int) -> int:
    left = max(weights)
    right = sum(weights)

    while left < right:
        mid = (left + right) // 2

        if can_ship(weights, mid, days):
            right = mid
        else:
            left = mid + 1

    return left