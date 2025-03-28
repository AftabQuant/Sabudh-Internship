class MyQueue:
    def __init__(self):
        self.stack1 = []  # for pushing elements
        self.stack2 = []  # for popping elements

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self._transfer()
        return self.stack2.pop() if not self.empty() else None

    def peek(self) -> int:
        self._transfer()
        return self.stack2[-1] if not self.empty() else None

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def _transfer(self) -> None:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

def execute_operations(operations, values):
    results = [None]
    obj = None
    for op, val in zip(operations, values):
        if op == "MyQueue":
            obj = MyQueue()
        elif op == "push":
            obj.push(val[0])
        elif op == "pop":
            results.append(obj.pop())
        elif op == "peek":
            results.append(obj.peek())
        elif op == "empty":
            results.append(obj.empty())
    return results

operations = ["MyQueue", "push", "push", "peek", "pop", "empty"]
values = [[], [1], [2], [], [], []]
print(execute_operations(operations, values))