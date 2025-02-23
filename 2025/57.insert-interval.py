#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Medium (42.81%)
# Likes:    10850
# Dislikes: 860
# Total Accepted:    1.4M
# Total Submissions: 3.2M
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# You are given an array of non-overlapping intervals intervals where
# intervals[i] = [starti, endi] represent the start and the end of the i^th
# interval and intervals is sorted in ascending order by starti. You are also
# given an interval newInterval = [start, end] that represents the start and
# end of another interval.
# 
# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
# 
# Return intervals after the insertion.
# 
# Note that you don't need to modify intervals in-place. You can make a new
# array and return it.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# 
# 
# Constraints:
# 
# 
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^5
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals.append(newInterval)
        # intervals.sort()
        # ans = []
        # start_window = intervals[0][0]
        # end_window = intervals[0][1]        
        
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] > end_window:
        #         ans.append([start_window, end_window])
        #         start_window = intervals[i][0]
        #     end_window = max(end_window, intervals[i][1])

        # ans.append([start_window, end_window])
        # return ans
        ans = []
        for interval in intervals:
            if newInterval[1] < interval[0]:
                ans.append(newInterval)
                newInterval = interval
            elif newInterval[0] > interval[1]:
                ans.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        ans.append(newInterval)
        return ans
    


# @lc code=end

