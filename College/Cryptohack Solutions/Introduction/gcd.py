def gcd(a, b):
    if a==0:
        return b
    return gcd(b%a, a)

num1 = 66528
num2 = 52920

print(gcd(num1, num2))