class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def get_min(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

def execute_operations(operations, values):
    results = [None]
    obj = None
    for op, val in zip(operations, values):
        if op == "MinStack":
            obj = MinStack()
        elif op == "push":
            obj.push(val[0])
        elif op == "pop":
            obj.pop()
        elif op == "top":
            results.append(obj.top())
        elif op == "getMin":
            results.append(obj.get_min())
    return results

operations = ["MinStack","push","push","push","getMin","pop","top","getMin"]
values = [[],[-2],[0],[-3],[],[],[],[]]
print(execute_operations(operations, values))