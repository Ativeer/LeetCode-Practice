class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remaining_gas_required = 0
        i = 0
        while i < len(gas): 
            gas_total = 0
            for j in range(i, len(gas)):
                gas_total += (gas[j]-cost[j])
                if gas_total < 0:
                    
                    break
            if gas_total >= 0  and gas_total + remaining_gas_required >= 0:
                return i
            i = j + 1
            remaining_gas_required += gas_total
            
        return -1