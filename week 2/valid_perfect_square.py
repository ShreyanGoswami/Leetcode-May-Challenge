# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Follow up: Do not use any built-in library function such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left <= right:
            mid = (left + right) >> 1
            midSqr = mid ** 2
            if midSqr == num:
                return True
            elif midSqr > num:
                right = mid - 1
            else:
                left = mid + 1
        return False