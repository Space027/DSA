l1=[5,1,8,2,9,3]




def ans(l1):
    sort=True
    rev=False
    inp=input("normal or reverse? ")
    if inp=='normal':
        rev=False
    elif inp=='reverse':
        rev=True
    if rev==False:
        while sort==True:
            sort=False
            for i in range(1,len(l1)):
                if l1[i-1]>l1[i]:
                    t=l1[i]
                    l1[i]=l1[i-1]
                    l1[i-1]=t
                    sort=True

    if rev==True:
        while sort==True:
            sort=False
            for i in range(1,len(l1)):
                if l1[i-1]<l1[i]:
                    t=l1[i]
                    l1[i]=l1[i-1]
                    l1[i-1]=t
                    sort=True
    
ans(l1)
print(l1)