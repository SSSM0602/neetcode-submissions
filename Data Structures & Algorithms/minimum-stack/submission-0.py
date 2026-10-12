class MinStack:

    def __init__(self):
        self.lst = []
        self.minstk = []

    def push(self, val: int) -> None:
        self.lst.append(val)
        self.minstk.append(min(val, self.minstk[-1] if self.minstk else val))
        

    def pop(self) -> None:
        self.lst.pop()
        self.minstk.pop()
        

    def top(self) -> int:
        return self.lst[-1]
        

    def getMin(self) -> int:
        return self.minstk[-1]
        
