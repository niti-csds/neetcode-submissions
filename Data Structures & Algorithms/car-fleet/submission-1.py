class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        
        stack = []
        combo = [[n, k] for n, k in zip(position, speed)]
        combo.sort()
        for i in range(len(speed)):
            time = (target - combo[i][0])/combo[i][1]
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)
        