def hoji(n):
    if n == 0:
        return""
    return hoji(n//2) + str (n%2)

print(hoji(10))