class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            index = i
            while s[index] != '#':
                index += 1
            length = int(s[i:index])
            i = index + 1
            index = i + length
            res.append(s[i:index])
            i = index
        return res
