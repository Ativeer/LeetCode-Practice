class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        length = len(candidates)
        ans = []
        def helper(remaining_target, idx=0, temp=[]):
            if idx == length:
                return
            
            if remaining_target == 0:
                ans.append(temp)
                return
            
            if remaining_target < 0:
                return
            
            temp.append(candidates[idx])
            helper(remaining_target-candidates[idx], idx, temp.copy())
            temp.pop()
            helper(remaining_target, idx+1, temp.copy())
        helper(target)
        return ans