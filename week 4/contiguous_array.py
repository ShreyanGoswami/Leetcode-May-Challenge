# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

class Solution:
    
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        d[0] = -1
        count = 0
        maxCount = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in d:
                maxCount = max(maxCount, i - d[count])
            else:
                d[count] = i
        return maxCount
            