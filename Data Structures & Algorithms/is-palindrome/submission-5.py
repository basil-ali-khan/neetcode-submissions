class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        # print((i, j))

        while i < j:
            # print("s[i]", s[i], "   s[j]", s[j])
            # print("s[i].isalnum()", s[i].isalnum())
            # print("s[j].isalnum()", s[j].isalnum())
            
            if s[i].isalnum() and s[j].isalnum():
                # print("both true")
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
            
            elif s[i].isalnum() == False:
                # print("s[i] false")
                i += 1

            elif s[j].isalnum() == False:
                # print("s[j] false")
                j -= 1
        
        return True
        