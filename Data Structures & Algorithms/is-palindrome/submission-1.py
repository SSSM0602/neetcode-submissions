class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        
        
        s = re.sub(r'\W+', '', s).lower()
        print(s)
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l = l + 1
            r = r - 1
        return True