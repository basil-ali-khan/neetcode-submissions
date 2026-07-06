class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for i in s:
            if i in ds.keys():
                ds[i] += 1
            else:
                ds[i] = 1

        for i in t:
            if i in dt.keys():
                dt[i] += 1
            else:
                dt[i] = 1

        for i in ds.keys():
            if i in dt.keys(): 
                if ds[i] != dt[i]: 
                    return False
            else:
                return False

        for i in dt.keys():
            if i in ds.keys(): 
                if ds[i] != dt[i]: 
                    return False
            else:
                return False
            
        return True
        