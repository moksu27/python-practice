import sys
import numpy as np

def solution(matrix):
    answer=0
    global a0
    mid=len(a0)//2
    for i in range(0,len(a0)):
        c=list(matrix[i,:])
        c.sort()
        e=c[mid]
        f=list(matrix[i,:]).index(e)

        d=list(matrix[:,f])
        d.sort()
        if c[mid]==d[mid]:
            answer+=1
          
    return answer

input=sys.stdin.readline


a0=list(map(int,input().split()))
matrix=np.array([a0])
if len(a0)%2==1:
    for i in range(1,len(a0)):
        a1=list(map(int,input().split()))
        matrix=np.vstack([matrix,a1])

elif len(a0)%2==0:
    sys.exit()

print(solution(matrix))