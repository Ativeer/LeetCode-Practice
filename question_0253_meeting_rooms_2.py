class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end = [intervals[0][1]]
        m = end[0]
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            create = False
            for j in range(len(end)):
                if end[j] > start:
                    continue
                else:
                    end[j] = intervals[i][1]
                    create = True
                    break
            if not create:
                end.append(intervals[i][1])
        return len(end)