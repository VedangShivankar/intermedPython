
s = []
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('https://www.cnn.com/china')

s.pop()
print(s)
print(s[-1])

from collections import deque
stack1 = deque()

stack1.append("https://www.cnn.com/")
print(stack1)

class Stack:

    def __init__(self):
        self.container = deque()
        
    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop

    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

s = Stack()
s.push(5)

print(s.peek())
s.pop()
print(s.is_empty())

s.push(67)
s.push(7)
s.push(3457)

print(s.size())