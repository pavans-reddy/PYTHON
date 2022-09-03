#Numbers are relatively prime

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
mn = min(a, b)
for i in range(1, mn+1):
    if a % i == 0 and b % i == 0 :
        hcf = i
if hcf == 1:
    print(f"{a} and {b} are relatively prime.")
else:
    print(f"{a} and {b} are not relatively prime.")

