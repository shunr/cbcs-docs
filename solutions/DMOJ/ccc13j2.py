meme = list("IOSHZXN")
s = list(input())
aaa = True
for k in s:
    if k not in meme:
        aaa = False
        break;
        
print("YES" if aaa else "NO")