#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (56.99%)
# Likes:    30662
# Dislikes: 1930
# Total Accepted:    3.8M
# Total Submissions: 6.6M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
# 
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
# 
# Return the maximum amount of water a container can store.
# 
# Notice that you may not slant the container.
# 
# 
# Example 1:
# 
# 
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
# 
# 
# Example 2:
# 
# 
# Input: height = [1,1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        right_pos = len(height) - 1
        left_pos = 0
        max_area = 0
        while left_pos < right_pos:
            left_h = height[left_pos]
            right_h = height[right_pos]
            curr_area = min(left_h, right_h) * (right_pos - left_pos)
            max_area = max(max_area, curr_area)

            if left_h < right_h:
                left_pos += 1
            else:
                right_pos -= 1
        return max_area

# @lc code=end

