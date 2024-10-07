N, M = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
maks_P = max(P)
maks_C = max(C)
min_P = min(P)
min_C = min(C)

if(P>0 and C>0):
    positif_p = sum(p for p in P if p > 0)
    hasil = min_C-positif_p
elif(P<0 and C<0):
    negatif_c = sum(c for c in C if c < 0)
    hasil = min_P+negatif_c
elif(P<0 and C>0):
    hasil = maks_P-min_C
else:
    positif_p = sum(p for p in P if p > 0)
    negatif_c = sum(c for c in C if c < 0)
    hasil = negatif_c - positif_p

print(hasil)