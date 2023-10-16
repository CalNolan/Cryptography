def fermat(num1, num2):
    return num1**(num2-1)%num2
ans1 = fermat(27324678765465536, 65537)
print(ans1)