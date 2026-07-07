from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:

            lst = [0] * 26

            for char in word:
                lst[ord(char) - ord('a')] += 1

            d[tuple(lst)].append(word)

        return list(d.values())        