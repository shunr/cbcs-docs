s = input()
n = int(input())

mins = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
for i in range(len(s) - n):
    if s[i:i+n] < mins:
        mins = s[i:i+n]
print(mins)