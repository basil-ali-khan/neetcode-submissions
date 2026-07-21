class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        longest = 0
        
        for right in range(len(s)):
            # 1. Add current character to frequency map
            char = s[right]
            count[char] = count.get(char, 0) + 1
            
            # 2. Keep track of the highest frequency of any character in the current window
            max_freq = max(max_freq, count[char])
            
            # 3. Check if the window is invalid. 
            # If (total window size - most frequent char) > k, we have too many errors!
            while (right - left + 1) - max_freq > k:
                # Shrink from the left
                count[s[left]] -= 1
                left += 1
                
            # 4. Record the max valid window size
            longest = max(longest, right - left + 1)
            
        return longest