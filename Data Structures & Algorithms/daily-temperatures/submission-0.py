class Solution:
    def dailyTemperatures(self, tem: List[int]) -> List[int]:
        stack = []
        res = [0] * len(tem)
        for i in range(len(tem)):
            for j in range(i,len(tem)):
                if tem[j] > tem[i]:
                    res[i] = j - i  
                    break          
        return res