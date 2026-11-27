al = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
kl = "аабб"
l = len(kl)

tekst = open("t.txt").read().lower()
tekst = [s for s in tekst if s in al]

shifr = [
    al[(al.index(tekst[k]) + al.index(kl[k % l])) % len(al)]
    for k in range(len(tekst))
]
dlina_shifra = len(shifr)
kol_vo = [[shifr.count(z)/dlina_shifra, z]for z in al]
for f, x in kol_vo:pass
#print(x,f)
print(shifr)




