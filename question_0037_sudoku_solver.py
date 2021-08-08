from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, boxes = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                n = int(board[r][c])
                rows[r].add(n)
                cols[c].add(n)
                boxes[(r // 3) * 3 + c // 3].add(n)
        # print(boxes[3])
        def isSafe(number, pos_x, pos_y):
            pos = (pos_x // 3) * 3 + pos_y // 3
            return number not in boxes[pos] and number not in rows[pos_x] and number not in cols[pos_y]
        
        def backTrack(row, col):
            if row == 8 and col == 9:
                return True
            elif col == 9:
                col = 0
                row += 1
            
            if board[row][col] != ".":
                return backTrack(row, col+1)
            
            pos1 = (row // 3) * 3 + col // 3
            for n in range(1, 10):
                if isSafe(n, row, col):
                    board[row][col] = str(n)
                    rows[row].add(n)
                    cols[col].add(n)
                    boxes[pos1].add(n)
                    
                    if backTrack(row, col+1):
                        return True
                    else:
                        board[row][col] = "."
                        rows[row].remove(n)
                        cols[col].remove(n)
                        
                        boxes[pos1].remove(n)
                        
            return False 
            
        backTrack(0, 0)
        