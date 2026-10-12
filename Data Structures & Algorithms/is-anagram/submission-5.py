class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return len(s) == len(t) and Counter(s) == Counter(t)