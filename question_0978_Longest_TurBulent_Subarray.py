class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if not arr:
            return 0
        if len(arr) == 1:
            return 1
        
        if arr[0] == arr[1]:
            ans = 1
            temp = 1
        else:
            ans = 2
            temp = 2
        check = arr[0] > arr[1]
        # ans = 2
        # temp = 2
        for i in range(2, len(arr)):
            # print(temp, arr[i])
            if check:
                if arr[i] <= arr[i-1]:
                    ans = max(ans, temp)
                    if arr[i] == arr[i-1]:
                        temp = 1
                    else:
                        temp = 2
                    continue
                check = False
            else:
                if arr[i] >= arr[i-1]:
                    ans = max(ans, temp)
                    if arr[i] == arr[i-1]:
                        temp = 1
                    else:
                        temp = 2
                    continue
                check = True
            temp += 1
        ans = max(ans, temp)
        return ans