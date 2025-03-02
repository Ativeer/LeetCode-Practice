#
# @lc app=leetcode id=1424 lang=python3
#
# [1424] Diagonal Traverse II
#
# https://leetcode.com/problems/diagonal-traverse-ii/description/
#
# algorithms
# Medium (57.58%)
# Likes:    2240
# Dislikes: 155
# Total Accepted:    157.7K
# Total Submissions: 273.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a 2D integer array nums, return all elements of nums in diagonal order
# as shown in the below images.
# 
# 
# Example 1:
# 
# 
# Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,2,7,5,3,8,6,9]
# 
# 
# Example 2:
# 
# 
# Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i].length <= 10^5
# 1 <= sum(nums[i].length) <= 10^5
# 1 <= nums[i][j] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        q = deque()
        q.append([0, 0])
        ans = []
        while q:
            x, y = q.popleft()
            ans.append(nums[x][y])

            if y == 0 and x + 1 < len(nums):
                q.append([x+1, y])
            
            if y + 1 < len(nums[x]):
                q.append([x, y+1])
        return ans

# @lc code=end

