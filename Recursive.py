# def number(n):
#     if n==0:
#         return 0
#     else:
#         return number(n-1)+n

# print(number(100))

# def numbe(n):
#     if n==0:
#         return 1
#     else:
#         return numbe(n-1)*n
    
# print(numbe(5))

# def numb(n1,n2):
#     if n2==0:
#         return 1
#     else:
#         return numb(n1,n2-1)*n1

# print(numb(0,3))

# def num(n):
#     if n==0:
#         return
    
#     print(n)
#     num(n-1) 
    
# num(5)

def nu(n,inp):
    if n>inp:
        return
    print(n)
    nu(n+1,inp)

nu(0,10)