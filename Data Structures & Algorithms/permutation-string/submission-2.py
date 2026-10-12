class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0, len(s1) - 1
        freq1, freq2 = [0] * 26, [0] * 26
        for c in s1:
            freq1[ord(c)-ord("a")] += 1

        while r < len(s2):
            freq2 = [0] * 26
            for c in s2[l:r+1]:
                freq2[ord(c)-ord("a")] += 1
            if freq1 != freq2:
                l += 1
                r = l + len(s1) - 1
            else:
                return True
        return False
        