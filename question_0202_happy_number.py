class Solution:
    def isHappy(self, n: int) -> bool:
        def find_sq(number):
            ans = 0
            while number > 0:
                r = number%10
                ans += r*r
                number = number//10
            return ans
        s = set()
        while True:
            n = find_sq(n)
            if n in s:
                return False
            if n == 1:
                return True
            else:
                s.add(n)
                
        return False



# Floyd Cycle Detection Algorithm

class Solution:
    def isHappy(self, n: int) -> bool:
        def find_numb_sq(number):
            s = 0
            while number > 0:
                d = number%10
                s += d*d
                number = number//10
            return s
        
        fastP = find_numb_sq(n)
        slowP = n
        while fastP != 1 and fastP != slowP:
            fastP = find_numb_sq(find_numb_sq(fastP))
            slowP = find_numb_sq(slowP)
        return fastP == 1