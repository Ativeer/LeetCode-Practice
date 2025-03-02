#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#
# https://leetcode.com/problems/interval-list-intersections/description/
#
# algorithms
# Medium (72.37%)
# Likes:    5699
# Dislikes: 121
# Total Accepted:    486.9K
# Total Submissions: 672.1K
# Testcase Example:  '[[0,2],[5,10],[13,23],[24,25]]\n[[1,5],[8,12],[15,24],[25,26]]'
#
# You are given two lists of closed intervals, firstList and secondList, where
# firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list
# of intervals is pairwise disjoint and in sorted order.
# 
# Return the intersection of these two interval lists.
# 
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with
# a <= x <= b.
# 
# The intersection of two closed intervals is a set of real numbers that are
# either empty or represented as a closed interval. For example, the
# intersection of [1, 3] and [2, 4] is [2, 3].
# 
# 
# Example 1:
# 
# 
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList =
# [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# 
# 
# Example 2:
# 
# 
# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= starti < endi <= 10^9
# endi < starti+1
# 0 <= startj < endj <= 10^9 
# endj < startj+1
# 
# 
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersectionInterval = []
        firstList.sort()
        secondList.sort()
        firstPtr = 0
        secondPtr = 0

        while firstPtr < len(firstList) and secondPtr < len(secondList):
            if self.__doesIntersect(firstList[firstPtr], secondList[secondPtr]):
                intersectionInterval.append(self.__findIntersection(firstList[firstPtr], secondList[secondPtr]))

            if firstList[firstPtr][1] > secondList[secondPtr][1]:
                secondPtr += 1
            else:
                firstPtr += 1
        
        return intersectionInterval


    
    def __doesIntersect(self, first: List[int], second: List[int]) -> bool:
        if second[0] <= first[0] <= second[1] or first[0] <= second[0] <= first[1]:
            return True
        return False
    
    def __findIntersection(self, first: List[int], second: List[int]) -> List[int]:
        return [max(first[0], second[0]), min(first[1], second[1])]

# @lc code=end

