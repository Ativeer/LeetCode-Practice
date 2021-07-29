class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = math.inf
        nums.sort()
        for i in range(len(nums)):
            start = i + 1
            end = len(nums)-1
            while end > start:
                sum_so_far = nums[i] + nums[start] + nums[end]
                if abs(target-sum_so_far) < abs(closest):
                    closest = target-sum_so_far
                if sum_so_far < target:
                    start += 1
                else:
                    end -= 1
            if closest == 0:
                return target
        return target - closest