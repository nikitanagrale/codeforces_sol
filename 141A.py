a=list(input())
b=list(input())
c=list(input())
c.sort()
l=a+b
l.sort()
if (l==c):
    print('YES')
else:
    print('NO')
