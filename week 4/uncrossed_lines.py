# We write the integers of A and B (in the order they are given) on two separate horizontal lines.

# Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

# A[i] == B[j];
# The line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

# Return the maximum number of connecting lines we can draw in this way.

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = []
        for i in range(len(B) + 1):
            dp.append([0] * (len(A) + 1))
        total = 0
        for i in range(1, (len(B) + 1)):
            for j in range(1, (len(A) + 1)):
                if A[j-1] == B[i-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    if dp[i][j] > total:
                        total = dp[i][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return total