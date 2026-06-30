import numpy as np 

sqrt_two = 2**(1/2)

def half_angle(val):
    return ((val+1)/2)**(1/2)

def cos_small(n):

    if n==1:
        base_val = sqrt_two/2
        return base_val
    else:
        next = half_angle(cos_small(n-1))
        return next


#test = cos_small(2)
#print(test)

def cos_small_iter(n):
    base_val = sqrt_two/2
    small_cos = half_angle(base_val)
    for i in range(1,n):
        small_cos = half_angle(small_cos)
    return(small_cos)

#test_iter = cos_small_iter(3)
#print(test_iter)


def pi_appr(n):
    P = (2*(1-cos_small(n)))**(1/2)
    return 2**(n+1)*P

#test_p = pi_appr(2)
#print(test_p)
#print(8*np.sqrt(2*(1-0.9238795325112867)))

#print(np.pi)

def pi_appr_iter(n):
    P = (2*(1-cos_small_iter(n)))**(1/2)
    return 2**(n+2)*P


def n_test(lvl):
    
    n=1
    diff = pi_appr(n)-np.pi

    while np.abs(diff)>lvl:
        n = n+1
        diff = pi_appr(n)-np.pi                
    return diff,n
    
#print(n_test(0.00000001))

#print(pi_appr(13))
#print(np.pi)
    
def n_test_iter(lvl):
    
    n=1
    diff = pi_appr_iter(n)-np.pi

    while np.abs(diff)>lvl:
        n = n+1
        diff = pi_appr_iter(n)-np.pi                
    return diff,n

test = pi_appr_iter(45)
print(test)

def find_max(lvl):
    

    for i in range(1,lvl):
        print(cos_small_iter(i), pi_appr_iter(i), i)
        i += 1
        
    
#find_max(44) cos_small bliver 1 ved n==26, men bliver værre efter n==19 også :(

print(pi_appr_iter(13))
print(np.pi)
print(pi_appr(25))