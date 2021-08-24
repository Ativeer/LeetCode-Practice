import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        index = [0 for _ in range(len(matrix))]
        bucket = [(matrix[i][0], i) for i in range(len(matrix))]
        heapq.heapify(bucket)
        count = 1
        while count < k:
            element, row = heapq.heappop(bucket)
            position = index[row]
            
            count += 1
            if position == len(matrix[0])-1:
                continue
            heapq.heappush(bucket, (matrix[row][position+1], row))
            index[row] += 1
            
        return heapq.heappop(bucket)[0]