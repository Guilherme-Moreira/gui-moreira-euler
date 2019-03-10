n = []
for i in range(1, 1000000):
    n.append(str(i))

n = ''.join(n)

a = int(n[0])
b = int(n[9])
c = int(n[99])
d = int(n[999])
e = int(n[9999])
f = int(n[99999])
g = int(n[999999])

print(a*b*c*d*e*f*g)  # 210

# This is a very ugly solution, but runs very quickly
