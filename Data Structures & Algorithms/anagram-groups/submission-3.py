class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            curr = strs[i]
            curr_sorted = "".join(sorted(strs[i]))
            # if curr in d:
            #     continue
            # else:
            #     d[curr] = []

            if curr_sorted not in d:
                d[curr_sorted] = [curr]
            else:
                d[curr_sorted].append(curr)

        # print(d)
        ret_lst = []
        for i in d:
            ret_lst.append(d[i])
        
        return ret_lst