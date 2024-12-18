def isPrime(num):
    for x in range(num-1,1,-1):
        if num%x==0:
            return False
    else:
        return True 

def findDistance(num):
    while not isPrime(num):
        x = 2
        while num%x != 0:
            x+=1
        num = num//x
    return num 

      
     

print(findDistance(6))