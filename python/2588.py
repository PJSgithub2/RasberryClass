a = int(input())
b = int(input())


c = int(a) * int(b%10)
d = int(a) * int(b//10%10)
e = int(a) *int(b//100)

print(c)
print(d)
print(e)
print(c+(d*10)+(e*100))
