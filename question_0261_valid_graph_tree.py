class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = {i:i for i in range(n)}
        for edge in edges:
            
            if d[edge[0]] == d[edge[1]]:
                # cycle detected
                return False
            else:
                convert = d[edge[0]]
                revert = d[edge[1]]
                for i in d:
                    if d[i] == convert:
                        d[i] = revert
                                    
            # print(edge, d)
        compare = d[0]
        # print(d)
        for i in d:
            if d[i] != compare:
                # Two components detected
                return False
        return True