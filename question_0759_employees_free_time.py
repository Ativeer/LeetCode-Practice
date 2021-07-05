"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':        
        work_time = []
        for s in schedule:
            for i in s:
                work_time.append([i.start, i.end])
        work_time.sort()
        final_ans = []
        s = Interval(-math.inf, math.inf)
        final_ans.append(s)
        
        for i in range(len(work_time)):
            start = work_time[i][0]
            end = work_time[i][1]
            e = -math.inf
            
            for j in range(len(final_ans)):
                if final_ans[j].end >= start:
                    if final_ans[j].start < start:
                        e = final_ans[j].end
                        final_ans[j].end = start 
                    break
            if e >= math.inf:
                
                new = Interval(end, math.inf)
                final_ans.append(new)
                continue
            
            for k in range(j, len(final_ans)):
                if final_ans[k].start <= end:
                    if final_ans[k].end >= end:
                        final_ans[k].start = end
            
        
        return final_ans[1:-1]