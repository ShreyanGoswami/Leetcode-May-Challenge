# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        res = []
        start = 0
        end = len(p)
        p = Counter(p)
        toCheck = Counter(s[start:end])
        while end <= len(s):
            if toCheck == p:
                res.append(start)
                toCheck[s[start]] -= 1
                if toCheck[s[start]] == 0:
                    del toCheck[s[start]]
                if end == len(s):
                    break
                start += 1
                end += 1
                try:
                    toCheck[s[end-1]] +=1
                except KeyError:
                    toCheck[s[end-1]] = 1
            else:
                start += 1
                end += 1
                toCheck = Counter(s[start:end])
        return res