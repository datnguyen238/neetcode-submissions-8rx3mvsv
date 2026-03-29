class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Input: a string of characters
        # Output: an integer (showing the longest subsequent)

        if not s:
            return 0
        
        seen = set()
        i = 0 
        res  = 0
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            res = max(res, j-i+1)
        return res