N, M = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

maks_P = max(P)
maks_C = max(C)
min_P = min(P)
min_C = min(C)

if all(p > 0 for p in P) and all(c > 0 for c in C):
    positif_p = sum(P)
    hasil = min_C - positif_p
elif all(p < 0 for p in P) and all(c < 0 for c in C):
    negatif_c = sum(C)
    hasil = negatif_c - maks_P
elif all(p < 0 for p in P) and all(c > 0 for c in C):
    hasil = min_C - maks_P
    if min_C > maks_P:
        hasil = 0
    else:
        print(hasil)
else:
    positif_p = sum(p for p in P if p > 0)
    negatif_c = sum(c for c in C if c < 0)
    hasil = negatif_c - positif_p

print(hasil)