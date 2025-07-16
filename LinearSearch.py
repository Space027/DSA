l1=[3,7,1,9,12,34,6,2,56,1,5]
item=input("Choose a number: ")
item=int(item)

for i in range(len(l1)):
    if item!=l1[i]:
        i+=1
        if i>=len(l1):
            print("YOUR NUMBER HAS NOT BEEN FOUND")
    elif item==l1[i]:
        print("YOUR NUMBER HAS BEEN FOUND\nTHE INDEX NUMBER IS",i)
        break