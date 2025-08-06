class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,inp):
        self.queue.append(inp)
    def dequeue(self):
        if len(self.queue)==0:
            print("CANNOT DEQUEUE")
        else:
            self.queue.pop(0)
    def front(self):
        return (self.queue[0])
    def rear(self):
        return (self.queue[len(self.queue)-1])
    def isEmpty(self):
        emptiness=True
        if len(self.queue)>0:
            emptiness=False
        if emptiness==True:
            print(True)
        else:
            print(False)
    def size(self):
        return (len(self.queue))
    def print(self):
        print(self.queue)

# q1=Queue()

# q1.enqueue('a')
# q1.enqueue('H')
# q1.enqueue(99)
# q1.enqueue('%')
# q1.enqueue('hey')
# q1.print()
# q1.size()
# q1.isEmpty()
# q1.dequeue()
# q1.print()
# q1.front()
# q1.rear()
# q1.dequeue()
# q1.dequeue()
# q1.dequeue()
# q1.print()
# q1.front()
# q1.dequeue()
# q1.isEmpty()