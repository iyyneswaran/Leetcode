# find the find occurrence of the target: 
def linear_Search(nums: list[int], target: int) -> int:
    for i, num in enumerate(nums):
        if num == target:
            return i

    return -1

# find all occurrences of the target:
def linear_Search_all(nums: list[int], target: int) -> list[int]:
    occurrences = []
    for i, num in enumerate(nums):
        if num == target:
            occurrences.append(i)

    return occurrences