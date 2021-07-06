

cases=int(input())

for i in range(cases):
    d,x,y,z=[int(x) for x in input().split()] 
    val1=(7*x)
    val2=(y*d)+(z*(7-d))
    print(max(val1,val2))
print('abc')
