#Ques.3

input_val = [[1, 1, 0, 0, 1, 1],
             [0, 1, 0, 1, 0, 0],
             [1, 1, 1, 0, 1, 0]]

list(map(sum, zip(*input_val)))

even_count, odd_count = 0, 0

for num in output_val: 

    if num % 2 == 0: 
        even_count += 1

    else: 
        odd_count += 1

print("Even column in the matrix: ", even_count) 
print("Odd column in the matrix: ", odd_count)
