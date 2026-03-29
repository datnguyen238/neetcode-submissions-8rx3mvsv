class MinStack:

    def __init__(self):
        self.stack = deque()
        self.mini = []


    def push(self, val: int) -> None:
        self.stack.appendleft(val)
        if self.mini:
            val = min(val, self.mini[-1])
        self.mini.append(val)
            
    def pop(self) -> None:
        a = self.stack.popleft()   
        if self.mini: 
            self.mini.pop()

    def top(self) -> int:
        return self.stack[0]
        

    def getMin(self) -> int:
        return self.mini[-1]
        

        
