class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        stack = []
        closerMap = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in closerMap:
                if stack and stack[-1] == closerMap[c]: stack.pop()
                else: return False
            else:
                stack.append(c)
        return True if not stack else False
        