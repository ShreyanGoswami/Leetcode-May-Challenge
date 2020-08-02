# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.

class Solution:
    
    def findMin(num1: str, num2: str) -> str:
        if int(num1) > int(num2):
            return num1
        return num2
    
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        s = []
        for x in num:
            if len(s) == 0:
                s.append(x)
            else:
                while k > 0 and len(s) > 0:
                    topOfStack = s[len(s) - 1]
                    if topOfStack > x:
                        s.pop()
                        k -= 1
                    else:
                        break
                s.append(x)
        while k != 0:
            s.pop()
            k -= 1
        res = ''.join(x for x in s).lstrip('0')
        if len(res) == 0:
            return '0'
        return res