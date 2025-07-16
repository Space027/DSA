l1=[3,7,1,9,12,34,6,2,56,90,5]
l1.sort()
item=input("Choose a number: ")
item=int(item)

l=0
h=len(l1)-1
found=False

while l<=h:
    mid=(l+h)//2
    if item==l1[mid]:
        found=True
        print("YOUR NUMBER HAS BEEN FOUND\nTHE INDEX NUMBER IS",mid)
        break
    elif item<l1[mid]:
        h=mid-1
    elif item>l1[mid]:
        l=mid+1

if found==False:
    print("YOUR NUMBER HAS NOT BEEN FOUND")
    