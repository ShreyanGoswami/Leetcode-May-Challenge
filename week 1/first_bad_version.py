# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. 
# You should minimize the number of calls to the API.

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        vers = isBadVersion
        high = n
        low = 1
        while True:
            mid = ( high+low )>>1
            isVersionBad = vers(mid)
            if isVersionBad == False:
                low = mid + 1
                if vers(low) == True:
                    return low
            else:
                isPreviousVersionBad = vers(mid-1)
                if  isPreviousVersionBad == False:
                    return mid
                high = mid - 1