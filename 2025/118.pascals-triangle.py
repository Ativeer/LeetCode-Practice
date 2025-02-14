#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (76.26%)
# Likes:    13485
# Dislikes: 495
# Total Accepted:    2M
# Total Submissions: 2.6M
# Testcase Example:  '5'
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
# 
# 
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= numRows <= 30
# 
# 
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def generate_pascal_row_entry(prev_row_val):
            curr_row = [1]
            values_to_calculate = len(prev_row_val) - 1
            for i in range(values_to_calculate):
                curr_val = prev_row_val[i+1] + prev_row_val[i]
                curr_row.append(curr_val)
            curr_row.append(1)
            return curr_row
        
        ans = [[1]]
        
        for i in range(1, numRows):
            prev_row = ans[i-1]
            next_row = generate_pascal_row_entry(prev_row)
            ans.append(next_row)
        return ans

# @lc code=end

