# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        n = len(nums) >> 1
        for k,v in d.items():
            if v > n:
                return k