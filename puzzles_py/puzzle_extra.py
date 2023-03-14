'''Write a function that takes in a non-empty array of
distinct integers and an integer representing a target
sum. 
If any two numbers in the input array sum up to the 
target sum, the function should return them in an 
array, in any order. 
If no two numbers sum up to the target sum, the 
function should return an empty array.
Note that the target sum must be obtained by summing 
two different integers in the array. 
You can´t add a single integer to itself to obtain 
the target sum.

Sample input
array = [3,5,-4,8,11,1,-1,6]
targetSum = 10
Output[-1,11]'''

'''Ideal Solution 
We need to evaluate how similar it is and the
thought process'''

"""
array = [3,5,-4,8,11,1,-1,6]
targetSum = 10
def twoNumberSum(array,targetSum):
    numbers = []
    table = []
    
    for x in array:
        print(x)
        z = targetSum - x
        print(z)
        if z in table:
            numbers.append(x)
            numbers.append(z)
           # print("jelou")
            return numbers
        else:
            table.append(x)
          #  print("checking")
            return numbers

print(twoNumberSum(array,targetSum))
"""



"""

arr = [3,5,-4,8,11,1,-1,6]
target = 10
n = len(arr)
print(n)
def add_sum(arr):
    l = []
    for i in range(n):
        print(i)
        for j in range(i+1, n):
            if (arr[i] + arr[j]) == target:
               # print(j)
                l.append(arr[i])
                l.append(arr[j])
                return l
            else:
                return l


print(add_sum(arr))

"""

arr = [3,5,-4,8,11,1,-1,6]
target = 10
n = len(arr)
print(n)
for i in range(n):
    print(" ")
    print(i) 
    
    for j in range(i+1, n):
        print(j)
        print("holi")
        L = arr[i]
        print(L)
        M = arr[j]
        print(M)
        print("bye")
        K = L + M
        print("respuesta",K)



