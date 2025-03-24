import math

p, q = map(int, input().split())
dalikliaiq = set()
rodiklis = 0

for i in range(1, int(math.sqrt(p)+1)):
    if p%i==0:
        dalikliaiq.add(int(i))
        if i!=p/i:
            dalikliaiq.add(int(p/i))

dalikliaiq=sorted(dalikliaiq)
bendri = [d for d in dalikliaiq if math.gcd(d, q) == 1]
print(" ".join(map(str, bendri)))