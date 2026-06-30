def fact(n:int)->int:
    if n==0 or n==1:
        return 1
    else:
       return fact(n-1)*n         
    
k=10
def summand(n:int, a,b):
    expo = 2*n+1
    nmrt=b**expo-a**expo
    dnmnt=fact(n)*expo
    return (-1)**n*nmrt/dnmnt

print(summand(100,5,1))
print(summand(75,5,1))

k=50
while abs(summand(k,10,0))>0.00001:
    print(summand(k,10,0),k) #k=68 er det højeste led, jeg behøver.
    k+=1

def gaus_int(a,b,n_o_t):
    return sum(summand(n,b,a) for n in range(0,n_o_t))

print(gaus_int(0,10,900))
