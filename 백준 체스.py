import sys
input=sys.stdin.readline

def function (x,y,z): # x=찾은 피스 개수, y=필요한 개수, z=정상 피스 개수
    while True:
        if x==z:
            break
        elif x<z:
            x+=1
            y+=1
        elif x>z:
            x-=1
            y-=1
    return (y)


a,b,c,d,e,f=map(int,input().split())
a2=b2=c2=d2=e2=f2=0

print(function(a,a2,1))
print(function(b,b2,1))
print(function(c,c2,2))
print(function(d,d2,2))
print(function(e,e2,2))
print(function(f,f2,8))

