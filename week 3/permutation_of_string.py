# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        start = 0
        end = len(s1)
        sdict = Counter(s1)
        while True:
            d = Counter(s2[start:end])
            
            if d == sdict:
                return True
            else:
                start += 1
                end += 1
                if end > len(s2):
                    return False
        