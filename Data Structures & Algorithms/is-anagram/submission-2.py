class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_list = list(t)
        # print(t_list)

        if len(s) < len(t):
            return False
        for i in s:
            if i not in t_list:
                return False

            t_list.remove(i)
        
        return True