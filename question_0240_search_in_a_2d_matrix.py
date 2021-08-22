class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(pos, column=False):
            start = pos
            end = len(matrix[0])-1 if column else len(matrix)-1
            while end >= start:
                mid = start + ((end-start)//2)
                
                compare = matrix[pos][mid] if column else matrix[mid][pos]
                
                if compare == target:
                    return True
                elif compare < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return False
        
        
        for i in range(min(len(matrix), len(matrix[0]))):
            
            if binarySearch(i) or binarySearch(i, True):
                return True
        return False

### APPROACH 2
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) - 1
        col = 0
        while row >= 0 and col < len(matrix[0]):

            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
            start_pos = (row, col)
        return False