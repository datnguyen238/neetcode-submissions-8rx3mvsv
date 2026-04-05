class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        check = set()
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            current = nums[i]
            r = len(nums) - 1
            l = i + 1
            while l < r:
                if current + nums[l] + nums[r] == 0:
                    if (current, nums[l], nums[r]) not in check:
                        res.append([current, nums[l], nums[r]])
                        check.add((current, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > -current:
                    r -= 1
                elif nums[l] + nums[r] < -current:
                    l += 1
                
        return res