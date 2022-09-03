#Euclidean Algorithm - greatest common divisor(GCD)
print("Enter two numbers: ")
a = int(input())
b = int(input())
r = a % b
while r > 0 :
    r = a % b
    a = b
    b = r
print(f"GCD is {a}")
