from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        letter_count = Counter(candidates)
        letter_count = [(i, letter_count[i]) for i in letter_count]
        length = len(letter_count)
        ans = []
        
        def helper(letter_count, remaining_target, temp=[], idx=0):
            if remaining_target == 0:
                ans.append(temp)
                return
            
            if remaining_target < 0:
                return
            
            for i in range(idx, length):
                num, f = letter_count[i]
                if f <= 0:
                    continue
                
                temp.append(num)
                letter_count[i] = (num, f-1)
                helper(letter_count, remaining_target-num, temp.copy(), i)
                letter_count[i] = (num, f)
                temp.pop()
        helper(letter_count, target)
        return ans