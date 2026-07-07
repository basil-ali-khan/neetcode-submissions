from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Create a frequency array for the 26 lowercase English letters
            count = [0] * 26
            
            for char in word:
                # Map 'a' to index 0, 'b' to index 1, ..., 'z' to index 25
                count[ord(char) - ord('a')] += 1
                
            # Convert the list to an immutable tuple so it can be used as a dictionary key
            anagram_map[tuple(count)].append(word)
            
        return list(anagram_map.values())