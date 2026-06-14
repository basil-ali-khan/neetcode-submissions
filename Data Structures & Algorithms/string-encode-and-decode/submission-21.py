class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string
        return s

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        n = len(s)
        
        while i < n:
            # 1. Find the delimiter '#' to handle multi-digit lengths safely
            j = i
            while s[j] != '#':
                j += 1
            
            # 2. Extract the length (everything from i up to j)
            curr_str_length = int(s[i:j])
            
            # 3. The string starts right after the '#' sign
            curr_str_index = j + 1
            
            # 4. Slice using the correct start and end boundaries
            curr_str = s[curr_str_index : curr_str_index + curr_str_length]
            lst.append(curr_str)
            
            # 5. Shift pointer i to the start of the next length prefix
            i = curr_str_index + curr_str_length

        return lst