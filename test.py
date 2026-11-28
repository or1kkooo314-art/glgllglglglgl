d = 10
sh = 10
shagi = 20
pole = [[0] * sh for y in range(d)]
for x, y in [(0,1),(1,2),(2,0),(2,1),(2,2)]:
    pole[x][y] = 1

for shag in range(shagi):
    print(shag)
    for s in pole:
        for e in s:
            print(e, end = " ")
        print()

    nov_pole = [[0] * sh for y in range(d)]
#     -1 0 1
#  -1
#  0
#  1
    for x in range(d):
        for y in range(sh):

            n = 0
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if not (dx == 0 and dy == 0):
                        xx = x + dx
                        yy = y + dy
                        if 0 <= xx < d and 0 <= yy < sh:
                            n += pole[xx][yy]
            if pole[x][y] == 0 and n == 3:
                nov_pole[x][y] = 1
            elif pole[x][y] == 1 and (n == 2 or n == 3):
                nov_pole[x][y] = 1

    pole = nov_pole
