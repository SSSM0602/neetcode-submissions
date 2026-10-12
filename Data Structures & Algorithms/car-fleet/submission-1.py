class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = dict(zip(position, speed))
        cars = dict(sorted(cars.items(), reverse=True))
        for pos, speed in cars.items():
            time = (target - pos) / speed
            stack.append(time)
            if len(stack) >= 2 and time <= stack[-2]:
                stack.pop()
            
        return len(stack)