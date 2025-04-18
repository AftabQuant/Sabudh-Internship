from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft() if not self.empty() else None

    def top(self) -> int:
        return self.q1[0] if not self.empty() else None

    def empty(self) -> bool:
        return len(self.q1) == 0

def execute_operations(operations, values):
    results = [None]
    obj = None
    for op, val in zip(operations, values):
        if op == "MyStack":
            obj = MyStack()
        elif op == "push":
            obj.push(val[0])
        elif op == "pop":
            results.append(obj.pop())
        elif op == "top":
            results.append(obj.top())
        elif op == "empty":
            results.append(obj.empty())
    return results

operations = ["MyStack", "push", "push", "top", "pop", "empty"]
values = [[], [1], [2], [], [], []]
print(execute_operations(operations, values))