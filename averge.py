import sys
input=sys.stdin.readline
def solution(queue1, queue2):
    d=0
    global ave, sum1
    while (True):
        if len(queue1)+len(queue2)>=d:
            if sum(queue1) > ave:
                c=queue1.pop(0)
                queue2.append(c)
                d+=1
            elif sum(queue1) < ave:
                c=queue2.pop(0)
                queue1.append(c)
                d+=1
            elif sum(queue1) == ave:
                return d
        else:
            return -1


a= list(map(int,input().split()))
b= list(map(int,input().split()))

sum1=sum(a)+sum(b)
ave=sum1//2

print(solution(a,b))