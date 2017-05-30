marks = []
n = int(input())
for i in range(n):
    marks.append(int(input()))

marks.sort()
if n % 2 == 0:
    print(round((marks[int(n/2)-1] + marks[int(n/2)])/2+0.1))
else:
    print(marks[int(n/2)])