# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

# Follow up: Your solution should run in O(log n) time and O(1) space.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid - 1] != nums[mid] and nums[mid + 1] != nums[mid]:
                return nums[mid]
            if nums[mid-1] == nums[mid]:
                left = mid + 1
            elif nums[mid+1] == nums[mid]:
                right = mid - 1