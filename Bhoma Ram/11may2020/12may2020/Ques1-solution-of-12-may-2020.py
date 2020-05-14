#Ques.1. adj_element_sum_prime

def prime(x):
    if x > 1:
        for i in range(2 , x//2):
            if(x%i)==0:
                return False
        else:
            return True
    else:
        return False
    
def adj_element_sum_prime(ls , n , m):
    count = 0
    for i in range(n):
        for j in range(m):
            sum = 0
            if 0 <= i-1:
                sum = sum+ls[i-1][j]
            if 0 <= j-1:
                sum = sum+sum+ls[i][j-1]
            if i+1 <= n-1:
                sum = sum+ls[i+1][j]
            if j+1 <= m-1:
                sum = sum+ls[i][j+1]
            if prime(sum):
                count = count+1
    return count
                
    
ls = []
n = int(input('enter row size:  '))
m = int(input('enter column size:  '))
for i in range(n):
    temp = []
    print('enter row' , i+1)
    for j in range(m):
        temp.append(int(input()))
    ls.append(temp)
print('\nOutput : ' , adj_element_sum_prime(ls , n , m))
