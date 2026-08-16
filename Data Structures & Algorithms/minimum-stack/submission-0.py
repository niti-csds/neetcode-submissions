class MinStack:

    def __init__(self):
        self.arr = []


    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        self.arr = self.arr[:-1]

    def top(self) -> int:
        return self.arr[-1]        

    def getMin(self) -> int:
        mini = self.arr[0]
        for n in self.arr:
            if n < mini:
                mini = n
        return mini

        
