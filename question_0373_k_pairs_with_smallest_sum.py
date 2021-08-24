import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[0]+nums2[0], 0, 0)]
        output = []
        visited = set((0,0))
        while len(output) < k and heap:
            res = heapq.heappop(heap)
            output.append([nums1[res[1]], nums2[res[2]]])
            
            if res[1] + 1 < len(nums1) and (res[1]+1, res[2]) not in visited:
                heapq.heappush(heap, (nums1[res[1]+1]+nums2[res[2]], res[1]+1, res[2]))
                visited.add((res[1]+1, res[2]))
                
            if res[2] + 1 < len(nums2) and (res[1], res[2]+1) not in visited:
                heapq.heappush(heap, (nums1[res[1]]+nums2[res[2]+1], res[1], res[2]+1))
                visited.add((res[1], res[2]+1))
        return output