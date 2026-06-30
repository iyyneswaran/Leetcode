def Game(Zi, B):
    for Z in Zi:
        energy_spent = (Z % 2) + (Z / 2)
        B -= energy_spent
        if B < 0:
            return 'NO'
    return 'YES'
    

B, n = map(int, input().split())
Zi = list(map(int, input().split()))
print(Game(Zi, B))