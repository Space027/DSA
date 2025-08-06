from Queues import Queue
from random import randint

game=Queue()

q1=int(input("HOW MANY PLAYERS? "))

for i in range(q1):
    q2=input("NAME "+str(i+1)+"? ")
    game.enqueue(q2)

while game.size()>1:
    passes=randint(1,game.size())
    for i in range(passes):
        f=game.front()
        game.dequeue()
        game.enqueue(f)
    print(game.front()+' got eliminated.')
    game.dequeue()

print("WINNER IS "+game.front())


