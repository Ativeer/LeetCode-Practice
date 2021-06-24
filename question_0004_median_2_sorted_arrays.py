class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged_array.append(nums1[i])
                i += 1
            else:
                merged_array.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            merged_array.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            merged_array.append(nums2[j])
            j += 1
        if len(merged_array) % 2 == 0:
            return (merged_array[len(merged_array)//2] + merged_array[(len(merged_array)//2)-1])/2
        return merged_array[len(merged_array)//2]