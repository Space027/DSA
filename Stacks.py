class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,num):
        self.stack.append(num)
    def pop(self):
        if len(self.stack)==0:
            print("No numbers left")
        else:
            self.stack.pop()
    def top(self):
        if len(self.stack)==0:
            print("No numbers left")
        else:
            print(self.stack[len(self.stack)-1])
    def size(self):
        print(len(self.stack))
    def display(self):
        print(self.stack)
    def empty(self):
        if len(self.stack)>0:
            return False
        else:
            return True
        
s1=Stack()
s1.push(10)
s1.push(56)
s1.push(2)
s1.push(5)
s1.push(13)
s1.display()
s1.pop()
s1.display()
s1.top()
s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.size()
print(s1.empty())
s1.pop()
s1.top()
s1.display()