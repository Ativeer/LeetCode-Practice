class Solution:
    def customSortString(self, order: str, str: str) -> str:
        bucket = [[] for _ in range(26)]
        for s in str:
            bucket[ord(s)-97].append(s)
            
        order_ans = ''
        for o in order:
            if bucket[ord(o)-97] == []:
                continue
            else:
                while bucket[ord(o)-97]:
                    order_ans += bucket[ord(o)-97].pop()
        
        for b in bucket:
            if b != []:
                while b:
                    order_ans += b.pop()
        return order_ans