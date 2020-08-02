# Given a positive integer num, output its complement number. 
# The complement strategy is to flip the bits of its binary representation.

class Solution:
    def findComplement(self, num: int) -> int:
        a = format(num, 'b')
        op = ''
        for x in a:
            if x == '0':
                op += '1'
            else:
                op += '0'
        return int(op, 2)