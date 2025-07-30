l1=[7,3,1,5,2,8]

def sort(l1):
    if len(l1)>1:
        mid=len(l1)//2
        left=l1[:mid]
        right=l1[mid:]
        print(l1)
        sort(left)
        sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                l1[k]=left[i]
                i+=1
            else:
                l1[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            l1[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            l1[k]=right[j]
            j+=1
            k+=1

sort(l1)
print(l1)
        