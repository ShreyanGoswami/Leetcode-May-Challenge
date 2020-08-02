# Given a string, sort it in decreasing order based on the frequency of characters.

class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        d = Counter(s)
        res = ''
        for k,v in d.most_common():
            res += k * v
        return res