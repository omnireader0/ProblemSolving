n = input()
l = len(n)//2
print("LUCKY" if sum(map(int, n[:l])) == sum(map(int, n[l:])) else "READY")