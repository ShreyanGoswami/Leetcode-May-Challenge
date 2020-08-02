# Given a m * n matrix of ones and zeros, 
# return how many square submatrices have all ones.

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        from collections import Counter
        dp = []
        m = len(matrix[0])
        total = 0
        for i in range(len(matrix)+1):
            dp.append([0]*(m+1))
        
        for i in range(1, len(matrix)+1):
            for j in range(1, m+1):
                if matrix[i-1][j-1] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i-1][j-1], dp[i][j-1])
                    total += dp[i][j]
            
        return total