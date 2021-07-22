class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dp_left = [math.inf for _ in range(len(dominoes))]
        dp_right = [math.inf for _ in range(len(dominoes))]
        left_count = 0
        right_count = 0
        last = False
        output = ""
        for i in range(len(dominoes)):
            if dominoes[i] == "R":
                dp_right[i] = 1
                right_count = 1
                last = "True"
            elif dominoes[i] == "L":
                
                
                right_count = 0
                last = False
            elif last:
                dp_right[i] = right_count+1
                right_count += 1
                last = "True"
                
        
        last = False
        for i in range(len(dominoes)-1, -1, -1):
            if dominoes[i] == "L":
                dp_left[i] = 1
                left_count = 1
                last = "True"
            elif dominoes[i] == "R":
                
                left_count = 0
                last = False
            elif last:
                dp_left[i] = left_count+1
                left_count += 1
                last = "True"
                
        
        for i in range(len(dominoes)):
            if dp_right[i] < dp_left[i]:
                add = "R"
            elif dp_right[i] > dp_left[i]:
                add = "L"
            else:
                add = "."
            output += add
        return output