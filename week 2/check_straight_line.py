# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
# Check if these points make a straight line in the XY plane.

class Solution:
    
    def calculateSlope(self, coord1, coord2):
        if coord2[0] == coord1[0]: return float('inf')
        return (coord2[1] - coord1[1])/(coord2[0] - coord1[0])
    
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 1 or n == 2:
            return True
        coord1 = coordinates[0]
        coord2 = coordinates[1]
        slope = self.calculateSlope(coord1, coord2)
        for i in range(2, n):
            if self.calculateSlope(coordinates[i], coordinates[i-1]) != slope:
                return False
        return True
        