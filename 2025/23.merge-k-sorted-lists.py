#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (55.50%)
# Likes:    20092
# Dislikes: 741
# Total Accepted:    2.4M
# Total Submissions: 4.2M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.
# 
# Merge all the linked-lists into one sorted linked-list and return it.
# 
# 
# Example 1:
# 
# 
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# 
# 
# Example 2:
# 
# 
# Input: lists = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: lists = [[]]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10^4.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        use heap
        '''
        # h = []
        # for ind, list_ in enumerate(lists):
        #     if not list_: continue
        #     # heapq.heappush(h, (list_.val, list_))
        #     h.append((list_.val, ind, list_))
        # # print(h)
        # heapq.heapify(h)

        # ans = ListNode()
        # temp = ans

        # while h:
        #     _, i, node = heapq.heappop(h)
        #     temp.next = node
        #     temp = temp.next
        #     if not node.next:
        #         continue
        #     heapq.heappush(h, (node.next.val, i, node.next))
        # return ans.next

        def merge(list1, list2):
            ans = ListNode()
            temp = ans
            while list1 and list2:
                if list2.val < list1.val:
                    temp.next = list2
                    list2 = list2.next
                else:
                    temp.next = list1
                    list1 = list1.next
                temp = temp.next
            
            if list1:
                temp.next = list1
            if list2:
                temp.next = list2
            return ans.next
        
        # cover base case
        if not lists or len(lists) == 0:
            return None
        
        if len(lists) <= 2:
            l1 = lists[0]
            l2 = lists[1] if len(lists) == 2 else None
            return merge(l1, l2)

        total_lists = len(lists)
        return merge(self.mergeKLists(lists[:total_lists//2]), self.mergeKLists(lists[total_lists//2:]))


        
        
        


# @lc code=end

