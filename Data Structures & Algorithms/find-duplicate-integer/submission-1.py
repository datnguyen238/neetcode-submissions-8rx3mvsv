class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return -1
        freq = Counter(nums)
        for num, count in freq.items():
            if count > 1:
                return num
        return -1