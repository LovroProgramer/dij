import heapq

# Učitavanje podataka
print("Zelite ucitati podatke 1/0")
izbor = int(input())

if izbor:
    with open('input.file.txt', 'r') as file:
        content = file.readlines()
        n, m = map(int, content[0].split())  # Prva linija sadrži n i m
        lista = []
        for line in content[1:]:  # Sve ostale linije predstavljaju a, b, c
            a, b, c = map(int, line.split())
            lista.append((a, b, c))
else:
    n, m = map(int, input().split())
    lista = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        lista.append((a, b, c))

# Kreiranje grafa
g = {}

for a, b, c in lista:
    if a not in g:
        g[a] = {}
    if b not in g:
        g[b] = {}
    if b in g[a]:
        g[a][b] = min(g[a][b], c)
    else:
        g[a][b] = c

# Dijkstra algoritam
def dijkstra(g, start):
    udaljenosti = {v: float('infinity') for v in g}
    udaljenosti[start] = 0
    visited = set()
    pq = [(0, start)]  # Prioritetni red s početnim čvorom i udaljenosti 0

    while pq:
        u, c = heapq.heappop(pq)
        if c in visited:
            continue
        visited.add(c)
        for c2, u2 in g[c].items():
            new_u = u + u2
            if new_u < udaljenosti[c2]:
                udaljenosti[c2] = new_u
                heapq.heappush(pq, (new_u, c2))
    return udaljenosti

# Pozivanje funkcije i ispis rezultata
rez = dijkstra(g, 1)
print(list(rez.values()))
