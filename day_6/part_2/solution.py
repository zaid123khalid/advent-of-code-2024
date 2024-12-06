import sys

sys.setrecursionlimit(10**6)

infile = "../input.txt"

p2 = 0

with open(infile, "r") as file:
    D = file.read().strip()

G = D.split("\n")
R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c] in "^>v<":
            sr, sc = r, c

for o_r in range(R):
    for o_c in range(C):
        if (o_r == sr and o_c == sc) or G[o_r][o_c] != ".":
            continue

        r, c = sr, sc
        d = {"^": 0, ">": 1, "v": 2, "<": 3}[G[sr][sc]]
        SEEN = set()

        while True:
            if (r, c, d) in SEEN:
                p2 += 1
                break
            SEEN.add((r, c, d))

            dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][d]
            rr, cc = r + dr, c + dc

            if not (0 <= rr < R and 0 <= cc < C):
                break

            if G[rr][cc] == "#" or (rr == o_r and cc == o_c):
                d = (d + 1) % 4
            else:
                r, c = rr, cc

print(p2)
