l1=[7,3,1,5,2,8]

for i in range(1,len(l1)):
    t=l1[i]
    v=i-1
    while v>=0 and t>l1[v]:
        l1[i]=l1[v]
        v-=1
    l1[v+1]=t
    print(l1)
print(l1)
            