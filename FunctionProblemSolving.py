# Function to find the maximum of three numbers
def maximum(x, y, z):
    if x > y and x > z:
        print("x is greatest number", x)
    elif y > z and y > x:
        print("y is greatest number", y)
    else:
        print("z is greatest number", z)

# Testing maximum function
maximum(8, 10, 6)     # y is greatest
maximum(10, 15, 40)   # z is greatest
maximum(45, 12, 23)   # x is greatest

print('-'*60)

# Function to create and print a list of squares from 1 to 30
def create_list():
    l = []
    for i in range(1, 31):
        l.append(i**2)   # append square of each number
    print(l)

create_list()

print('-'*60)

# Function to check if a number is prime
def check_prime(n):
    if n <= 1:
        print(n, "is not a prime number")
    else:
        for i in range(2, n):
            if n % i == 0:   # divisible by some number
                print(n, "is not a prime number")
                break
        else:
            print(n, "is a prime number")

# Testing prime check
check_prime(8)   # Not prime
check_prime(5)   # Prime
check_prime(2)   # Prime

print('-'*60)

# Function to find the sum of numbers in a list (using loop)
def number_sum(l):
    total = 0
    for i in l:
        total += i
    print(total)

number_sum([4, 5, 6, 8, 8, 9, 8, 8])   # Prints sum of list

# Function to find the sum of numbers in a list (using recursion)
def add(l):
    if len(l) == 1:       # Base case: only one element
        return l[0]
    else:                 # Recursive case
        return l[0] + add(l[1:])
    
print(add([4, 5, 6, 8, 8, 9, 8, 8]))   # Prints sum using recursion

print('-'*60)

# Function to print the nth term of Fibonacci series (using loop)
def fibonacci(n):
    first = 0
    second = 1
    for i in range(2, n):         # Iterative calculation
        result = first + second
        first = second
        second = result
    print(n, "th term of fibonacci series is:", result)

fibonacci(7)   # Prints 7th term of Fibonacci sequence

# Function to calculate Fibonacci number (using recursion)
def fs(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return (fs(num-1) + fs(num-2))

print(fs(10))   # Prints 10th Fibonacci number
