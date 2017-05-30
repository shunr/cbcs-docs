done = False
gg = ("dank", 100000)
while not done:
    k = input().split()
    if int(k[1]) < gg[1]:
        gg = (k[0], int(k[1]))
    if k[0] == "Waterloo":
        done = True
print(gg[0])