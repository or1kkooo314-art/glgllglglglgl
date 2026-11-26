sbornik1 = open("in1.txt",encoding = "utf-8").read().lower()
sbornik2 = open("in3.txt",encoding = "utf-8").read().lower()
sbornik3 = open("in2.txt",encoding = "utf-8").read().lower()

al = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
n = len(al)
sborniki = [sbornik1,sbornik2,sbornik3]

pary = [x+y for x in al for y in al]


res = []

for sbornik in sborniki:

    cnt = {p: 0 for p in pary}

    for i in range(len(sbornik) - 1):
        p = sbornik[i:i + 2]
        if p in cnt:
            cnt[p] += 1

    total = sum(cnt[p] for p in pary)

    res.append([cnt[p] / total if total > 0 else 0 for p in pary])

raz_tolstoy12 = sum(abs(res[0][x] - res[2][x]) for x in range(len(pary)))
raz_tolstoy1_dostoevskiy =sum(abs(res[0][x] - res[1][x]) for x in range(len(pary)))
raz_tolstoy2_dostoevskiy =sum(abs(res[2][x] - res[1][x]) for x in range(len(pary)))

exists = [
    x for x in range(len(pary))
    if res[0][x] > 0 or res[1][x] > 0 or res[2][x] > 0
]
for x in exists:
    print(pary[x],round(res[0][x], 6), round(res[1][x], 6), round(res[2][x], 6))

print(raz_tolstoy12)
print(raz_tolstoy2_dostoevskiy)
print(raz_tolstoy1_dostoevskiy)













