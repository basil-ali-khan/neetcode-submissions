class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            # If a duplicate is found, shrink the window from the left
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            # Add the current character and update the maximum length
            char_set.add(s[r])
            max_len = max(max_len, r - l + 1)
            
        return max_len