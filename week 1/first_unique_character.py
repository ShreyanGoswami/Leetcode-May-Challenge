# Given a string, find the first non-repeating character in it and return its index. 
# If it doesn't exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        d = Counter(s)
        for i in range(0, len(s)):
            if d[s[i]] == 1:
                return i
        return -1