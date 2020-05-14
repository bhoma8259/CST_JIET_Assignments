#Ques.2 find position of element in matrix.
x = int(input('enter number: ')) 
def search(mat, n, x):           
# set indexes for top right element Yaani i=0 and j=n-1 
    i = 0
    j = n - 1
    while ( i < n and j >= 0 ): 

        if (mat[i][j] == x ): 
            print(x , " Found at", '(' , i , "," , j , ')') 
            return 1
        
        if (mat[i][j] > x ): 
            j -= 1
            
        else: #YAANI  if mat[i][j] < x 
            i += 1
            
    print("Element not found") 
    return 0

# Driver Code 
mat = [ [10, 20, 30, 40], 
        [15, 25, 35, 45], 
        [27, 29, 37, 48], 
        [32, 33, 39, 50] ] 
search(mat, n, x) 

