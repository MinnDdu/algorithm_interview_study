
class Node:
    def __init__(self, item, next) -> None:
        self.item = item
        self.next = next

class Stack:
    def __init__(self) -> None:
        self.last = None
    
    def push(self, item) -> None:
        node = Node(item, self.last)
        self.last = node

    def pop(self) -> int:
        if self.last == None:
            print("The stack is empty")
        else:
            result = self.last.item
            self.last = self.last.next
            return result


s = Stack()
s.push(1)
s.push(2)

print(s.pop())
print(s.pop())
print(s.pop())


