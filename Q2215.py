class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        presence1 = set(nums1)
        presence2 = set(nums2)

        diff1 = []
        for num in presence1:
            if num not in presence2:
                diff1.append(num)

        diff2 = []
        for num in presence2:
            if num not in presence1:
                diff2.append(num)
       

        return [diff1, diff2]
    

# or 
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        presence1 = set(nums1)
        presence2 = set(nums2)

        diff1 = [num for num in presence1 if num not in presence2]
        diff2 = [num for num in presence2 if num not in presence1]

        return [diff1, diff2]