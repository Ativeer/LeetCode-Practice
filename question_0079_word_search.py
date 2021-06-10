class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for r in range(len(board)):
            for c in range((len(board[0]))):
                if board[r][c] == word[0]:
                    if self.dfs(r, c, board, word):
                        return True
        return False
    
    
    def dfs(self, row, column, l, letter):
        if len(letter) == 0:
            return True
        if row < 0 or row >= len(l) or column < 0 or column >= len(l[0]) or l[row][column] != letter[0]:
            return False
                
        l[row][column] = "#"
        ret = False
        for r, c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ret = self.dfs(row+r, column+c, l, letter[1:])
            if ret:
                break
        l[row][column] = letter[0]
        return ret

               
    