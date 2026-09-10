class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        curr_sum = 0
        check_map = {}

        for i in range(k):
            curr_sum += nums[i]
            check_map[nums[i]] = check_map.get(nums[i], 0) + 1

        if len(check_map) == k:
            max_sum = curr_sum

        for i in range(k, len(nums)):
            out_value = nums[i - k]
            curr_sum -= out_value
            check_map[out_value] -= 1
            if check_map[out_value] == 0:
                del check_map[out_value]

            in_value = nums[i]
            curr_sum += in_value
            check_map[in_value] = check_map.get(in_value, 0) + 1

            if len(check_map) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum
