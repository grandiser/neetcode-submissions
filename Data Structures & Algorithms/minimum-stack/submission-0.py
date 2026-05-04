class MinStack:

    def __init__(self):
        self.array = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.array.append(val)

        if len(self.array) == 1:
            self.min_val.append(val)
            return

        if val < self.min_val[-1]:
            self.min_val.append(val)
        else:
            self.min_val.append(self.min_val[-1])

    def pop(self) -> None:
        _ = self.array.pop()
        _ = self.min_val.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:

        return self.min_val[-1]
        
