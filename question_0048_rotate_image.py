class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        len_column = len(matrix[0])-1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_matrix[j][len_column-i] = matrix[i][j]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                matrix[i][j] = new_matrix[i][j]



# Constant space
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)-1
        for i in range(n+1):
            for j in range((n+1)//2):
                matrix[i][n-j], matrix[i][j] = matrix[i][j], matrix[i][n-j]
        
        for i in range(n+1):
            for j in range(n+1-i):
                matrix[i][j], matrix[n-j][n-i] = matrix[n-j][n-i], matrix[i][j]