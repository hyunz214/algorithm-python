def gcd(a, b):
    if a % b == 0 :
        return b
    else :
        c = a % b
        return gcd(b,c)

print(gcd(192, 162))