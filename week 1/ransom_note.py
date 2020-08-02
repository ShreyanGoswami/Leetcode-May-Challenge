# Given an arbitrary ransom note string and another string containing letters from  all the magazines, 
# write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
# Each letter in the magazine string can only be used once in your ransom note.

class Solution:
    
    def constructDict(self, s: str) -> dict:
        d = {}
        for x in s:
            try:
                d[x] += 1
            except KeyError:
                d[x] = 1
        return d
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = self.constructDict(ransomNote)
        
        for k, v in r.items():
            if magazine.count(k) < v:
                return False
        return True