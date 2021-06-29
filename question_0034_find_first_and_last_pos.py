class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstPos(nums, target):
            start = 0
            end = len(nums)-1
            
            while end >= start:
                mid = (end+start)//2
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    if mid == 0 or nums[mid-1] != nums[mid]:
                        return mid
                    else:
                        end = mid - 1
            return -1
        
        def lastPos(nums, target):
            start = 0
            end = len(nums)-1
            
            while end >= start:
                mid = (end+start)//2
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    if mid == len(nums)-1 or nums[mid+1] != nums[mid]:
                        return mid
                    else:
                        start = mid + 1
            return -1
        
        return [firstPos(nums, target), lastPos(nums, target)]