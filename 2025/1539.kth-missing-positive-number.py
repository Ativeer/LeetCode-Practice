#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#
# https://leetcode.com/problems/kth-missing-positive-number/description/
#
# algorithms
# Easy (61.62%)
# Likes:    7111
# Dislikes: 500
# Total Accepted:    586.1K
# Total Submissions: 949.2K
# Testcase Example:  '[2,3,4,7,11]\n5'
#
# Given an array arr of positive integers sorted in a strictly increasing
# order, and an integer k.
# 
# Return the k^th positive integer that is missing from this array.
# 
# 
# Example 1:
# 
# 
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The
# 5^th missing positive integer is 9.
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2^nd missing
# positive integer is 6.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length
# 
# 
# 
# Follow up:
# 
# Could you solve this problem in less than O(n) complexity?
# 
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # n = [i for i in range(len(arr)+ k)]

        # for num in arr:
        #     if num <= len(n):
        #         n[num-1] = -1
        
        # for k_, i in enumerate(n):
        #     if i != -1:
        #         k -= 1
        #         if k == 0:
        #             return k_ + 1

        start = 0
        end = len(arr)-1

        while start <= end:
            mid = start + (end - start) // 2
            mid_number = arr[mid]
            diff = mid_number - mid - 1
            # if diff == k:
            #     return mid_number - k
            if diff < k:
                # k -= diff
                start = mid + 1
            else:
                end = mid - 1
        return start + k


# @lc code=end

