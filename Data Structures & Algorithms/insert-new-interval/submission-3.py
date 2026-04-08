class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for i, curr in enumerate(intervals):
            if curr[1] < newInterval[0]:
                ans.append(curr)
            elif newInterval[1] < curr[0]:
                ans.append(newInterval)
                return ans + intervals[i:]
            else:
                newInterval[0] = min(curr[0],newInterval[0])
                newInterval[1] = max(curr[1],newInterval[1])

        ans.append(newInterval)
        return ans