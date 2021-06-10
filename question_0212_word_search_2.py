class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        end = "$"
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # set default value to either letter or {} if letter not in node
                node = node.setdefault(letter, {})
            node[end] = word
        print(trie)
        rows = len(board)
        column = len(board[0])
        
        similar = []
        
        def dfs(row, col, parent):
            letter = board[row][col]
            curr = parent[letter]
            
            word_ = curr.pop(end, False)
            
            if word_:
                similar.append(word_)
            board[row][col] = "#"
            
            for r, c in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                new_row = row + r
                new_col = col + c
                if new_row < 0 or new_col < 0 or new_row >= rows or new_col >= column:
                    continue
                if board[new_row][new_col] not in curr: continue
                dfs(new_row, new_col, curr)
                
            board[row][col] = letter
            
            # for optimization
            if not curr:
                parent.pop(letter)
                        
        for rw in range(rows):
            for cl in range(column):
                if board[rw][cl] in trie:
                    dfs(rw, cl, trie)
        return similar
