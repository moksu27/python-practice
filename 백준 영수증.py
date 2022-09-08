import sys
input=sys.stdin.readline

total=int(input())
kind=int(input())
sum=0

for i in range(kind):
    price,count=list(map(int,input().split()))
    sum=sum+price*count

if sum == total:
    print('Yes')
else:
    print('No')

