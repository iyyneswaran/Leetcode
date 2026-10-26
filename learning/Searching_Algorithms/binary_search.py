def binary_search(nums: list[int], target: int) -> int:
    l_ptr = 0
    r_ptr = len(nums) - 1

    while l_ptr <= r_ptr:
        m_ptr = (r_ptr + l_ptr) // 2

        if nums[m_ptr] == target:
            return m_ptr
        elif nums[m_ptr] < target:
            l_ptr = m_ptr + 1
        else:
            r_ptr = m_ptr - 1
            
    return -1