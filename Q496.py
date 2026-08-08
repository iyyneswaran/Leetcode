class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        length1, length2 = len(nums1), len(nums2)
        stack = [-1] * length1
        locations = {}
        for location, value in enumerate(nums2):
            if value not in locations:
                locations[value] = location
        i = 0
        while i < length1:
            index = locations[nums1[i]]
            while index < length2:
                if nums1[i] < nums2[index]:
                    stack[i] = nums2[index]
                    break
                else:
                    index += 1
            i += 1
        return stack


# optimal 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                greater[stack.pop()] = num
            stack.append(num)

        result = []
        for num in nums1:
            result.append(greater.get(num, -1))

        return result