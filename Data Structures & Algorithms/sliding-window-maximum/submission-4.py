class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        buffer = deque(nums[0:k])
        res = [max(buffer)]
        for i in range(k, len(nums)):
            buffer.popleft()
            buffer.append(nums[i])
            res.append(max(buffer))     
        return res 