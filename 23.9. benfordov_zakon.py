import random

pocty = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
pocty_percenta = {}

for i in range(1, 10001):
    c1 = random.randint(1, 100)
    c2 = random.randint(1, 100)
    nas = str(c1**c2)
    dig = int(nas[0])
    pocty[str(dig)] += 1

for pocet in pocty:
    pocty_percenta[pocet] = pocty[pocet] / 100
print(pocty)
print(pocty_percenta)
for x, y in pocty.items():
  print(x, y)

# pandas = datagrip virtualna tabulka dat v pocitaci, ma vela prikazov, vsetky funkcie co ma excel su tu




