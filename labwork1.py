#Ex1
import math
radius = int(input("Enter the radius: "))
cirlce = math.pi * radius**2 
print("The circle are is: ", cirlce)

#Ex2
C = int(input("enter the Celcius: "))
F = (C * 9 / 5) + 32
print("The Fahrenheit is: ", F)

#ex3
prime = int(input("Enter the number:"))
if prime <2:
    print("Not a prime")
else:
    for i in range(2,int(prime**0.5 +1)):
        if prime%i==0:
            print("Not a prime")
            break
    else:
         print("is prime")
         

#ex4
n = int(input("Enter a number: "))


if n <= 1:
    print(f"{n} is not a perfect number")
else:
    total_sum = 0

  
    for i in range(1, n):
        if n % i == 0:
            total_sum += i  

  
    if total_sum == n:
        print(f"{n} is a perfect number")
    else:
        print(f"{n} is not a perfect number")

#ex5
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]

fav_color = input("Enter your favorite color: ").strip().lower()

if fav_color in colors:
    index = colors.index(fav_color)
    print(f"Your color was found at index: {index}")
else:
    print("Sorry, I could not find your color")

#ex6
range1 = range(7)
range2 = range(1, 11, 3)
range3 = range(5, 0, -1)
range4 = range(6, -3, -2)

print("range1:", list(range1))
print("range2:", list(range2))
print("range3:", list(range3))
print("range4:", list(range4))

#ex7

def remove_dollar_sign(s):
    res = "" 
    for char in s:
        if char != "$":
            res += char  
    return res



text = "$100,000$ USD$"
print(remove_dollar_sign(text))  

#ex8
def extract_even(list):
    even_list =[]
    for i in list:
        if i % 2==0:
         even_list.append(i)
    return even_list
listt =[1, 2, 3,4 ,5 ,6,7,8,9]
print(extract_even(listt))

#ex9
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


number = int(input("Enter a non-negative integer: "))

print("Factorial:", factorial(number))

#ex10
def divisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


number = int(input("Enter a number: "))
divisors(number)

#ex11
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("Distance:", distance)

#ex12
def print_pattern(m, n):
    for i in range(m):
        if i == 0 or i == m - 1:
            print("* " * n)
        else:
            print("* ")


m = int(input("Enter m: "))
n = int(input("Enter n: "))

print_pattern(m, n)
