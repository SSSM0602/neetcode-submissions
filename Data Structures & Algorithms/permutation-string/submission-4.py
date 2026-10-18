class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l,r = 0, len(s1) - 1 
        freq1, freq2 = [0] * 26, [0] * 26
        for c in range(len(s1)):
            freq1[ord(s1[c])-ord("a")] += 1
            freq2[ord(s2[c])-ord("a")] += 1

        while r < len(s2) - 1:
            if freq1 == freq2:
                return True
            freq2[ord(s2[l]) - ord("a")] -= 1

            l += 1
            r += 1

            freq2[ord(s2[r]) - ord("a")] += 1
        
        return freq1 == freq2
