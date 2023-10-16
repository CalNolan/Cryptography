def exgcd(a, b):
    if a==0:
        return b, 0, 1

    gcd, x1, y1 = exgcd(b%a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y

num1 = 26513
num2 = 32321

dump, ans1, ans2 = exgcd(num1, num2)

if ans1<ans2:
    print(ans1)
else:
    print(ans2)