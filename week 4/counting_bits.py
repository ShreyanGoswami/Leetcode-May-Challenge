# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

class Solution:
    def countBits(self, num: int) -> List[int]:
        from collections import Counter
        lookup = {}
        res = []
        for i in range(0, 16):
            lookup[i] = Counter(bin(i))['1']
        
        for x in range(0, num + 1):
            binRepr = hex(x)
            count = 0
            while int(binRepr,16) != 0:
                keyToSearch = int(binRepr[-1],16) ^ 0000
                count += lookup[keyToSearch]
                binRepr = hex(int(binRepr,16) >> 4)
            res.append(count)
        return res