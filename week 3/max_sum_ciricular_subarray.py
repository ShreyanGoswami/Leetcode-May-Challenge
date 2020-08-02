# Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.
# Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
# Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

class Solution:
    def kadaneOptimized(self, arr):
        prevSum = next(arr)
        maxSum = prevSum
        for x in arr:
            prevSum = max(prevSum + x, x)
            maxSum = max(prevSum, maxSum)
        return maxSum
    
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        k = self.kadaneOptimized(iter(A))
        totalSum = sum(A)
        r = (x * -1 for x in A)
        kComplement = self.kadaneOptimized(r)
        totalSum = totalSum + kComplement
        if totalSum > k and totalSum != 0:
            return totalSum
        return k