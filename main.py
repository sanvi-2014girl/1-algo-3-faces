def function1(n):
    return n*(n+1) / 2
print(function1(5))

def function2(n):
    sum = 0
    for i in range(1,n+1):
         sum = sum+i
    return sum
print(function2(5))

def function3(n):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
             sum = sum+1
    return sum
print(function3(5))
#Method 1 is saving our time