def brojPutova(g, s, d, visited):
    if s == d:
        return 1  # Ako smo došli do ciljnog čvora, to je jedan put
    visited.add(s)
    count = 0
    for susjed in g[s]:
        if susjed not in visited:
            count += brojPutova(g, susjed, d, visited)
    visited.remove(s)
    return count

# Funkcija za pronalaženje broja alternativnih putova
def brojAlternativnihPutova(g, s, d):
    visited = set()  # Skup posjećenih čvorova
    broj_putova = brojPutova(g, s, d, visited)
    if broj_putova <= 1:
        return "Nema alternativnih putova."
    else:
        return f"Broj alternativnih putova: {broj_putova - 1}"

# Testiranje funkcije
broj_alt_putova = brojAlternativnihPutova(g, 1, 10)
print(broj_alt_putova)
