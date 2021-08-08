class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_array = [0 for _ in range(len(nums)+1)]
        prefix_array[1] = nums[0]
        for i in range(2, len(nums)+1):
            prefix_array[i] = prefix_array[i-1] + nums[i-1]
        
        start_pos = 0
        end_pos = 1
        min_length = len(nums) + 1
        while end_pos < len(prefix_array) and end_pos >= start_pos:
            cont_sum = prefix_array[end_pos] - prefix_array[start_pos]
            if target > cont_sum:
                end_pos += 1
            else:
                min_length = min(min_length, (end_pos-start_pos))
                start_pos += 1
        return min_length if min_length != len(nums)+1 else 0


# Approach 2
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = nums[0]
        start_pos = -1
        end_pos = 0
        min_length = len(nums) + 1
        while end_pos < len(nums):
            if s < target:
                end_pos += 1
                if end_pos == len(nums):
                    break
                s += nums[end_pos]
                
            else:
                min_length = min(min_length, end_pos - start_pos)
                start_pos += 1
                s -= nums[start_pos]
                
        return min_length if min_length != len(nums) + 1 else 0
        