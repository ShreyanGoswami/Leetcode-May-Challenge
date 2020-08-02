# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

# At the end, return the modified image.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        originalCol = image[sr][sc]
        q = []
        q.append([sr,sc])
        
        while len(q) != 0:
            row, col = q.pop()
            image[row][col] = newColor
            if row != 0:
                if image[row-1][col] == originalCol and image[row-1][col] != newColor: q.append([row-1, col])
            if row != len(image) - 1:
                if image[row+1][col] == originalCol and image[row+1][col] != newColor: q.append([row+1, col])
            if col != 0:
                if image[row][col-1] == originalCol and image[row][col-1] != newColor: q.append([row, col-1])
            if col != len(image[0]) - 1:
                if image[row][col+1] == originalCol and image[row][col+1] != newColor: q.append([row, col+1])
        
        return image