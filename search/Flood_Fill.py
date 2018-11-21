class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        n_row = len(image)
        n_col = len(image[0])
        stack = [(sr, sc)]
        oldColor = image[sr][sc]
        while stack:
            row, col = stack.pop()
            if image[row][col] == newColor:
                continue
            else:
                image[row][col] = newColor
                if row - 1 >= 0 and image[row - 1][col] == oldColor:
                    stack.append((row - 1, col))
                if row + 1 < n_row and image[row + 1][col] == oldColor:
                    stack.append((row + 1, col))
                if col - 1 >= 0 and image[row][col - 1] == oldColor:
                    stack.append((row, col - 1))
                if col + 1 < n_col and image[row][col + 1] == oldColor:
                    stack.append((row, col + 1))
        return image

