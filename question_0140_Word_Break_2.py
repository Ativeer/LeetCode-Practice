class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.trie = {}
        END = "$"
        for word in wordDict:
            node = self.trie
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node[END] = {}

        length = len(s)
        ans = []
        def helper(temp, counter, trie_node):
            
            if counter == (length):
                if temp not in ans:
                    if END in trie_node:
                        ans.append(temp)
                return
            
            if s[counter] not in trie_node:
                return
            
            temp += s[counter]
            trie_node = trie_node[s[counter]]
            if END in trie_node:
                if counter != (length-1):
                    helper(temp+" ", counter+1, self.trie)
                else:
                    helper(temp, counter+1, self.trie)
            helper(temp, counter+1, trie_node)

        
        helper("", 0, self.trie)
        return ans