"""
Given an array A1,A2…AN, find the minimum number of operations 
(possibly zero) required to convert all integers in A to 0.

In one operation, you

choose a non-negative integer p (p≥0),
select at most K indices in the array A, and
for each selected index i, replace Ai with Ai⊕2p. Here, ⊕ denotes 
bitwise XOR.

The first line contains an integer T - the number of test cases. Then 
T test cases follow.
The first line of each test case contains two integers N, K - the 
size of the array and the maximum number of elements you can select in 
an operation.
The second line of each test case contains N integers A1,A2…AN."""


# Solution Description
"""
1. Count odd numbers in the set. Check if the number is less than k.
2. XOR 
"""
cases=int(input())
passCase=[0,0,0]

for i in range(cases):
    n,k=[int(x) for x in input().split()] 
    a=list(map(int,input().split()))

    # while a!=passCase:


def xor(updatedList,i,p):
    """
    updatedList is the list holding values.
    i is the list of indices that will be XOR'ed. If i is not list, an error will be generated

    For e.g. 
    1. print(xor([3,6,10],[0],0)) --> [2, 6, 10]
    2. print(xor([2,6,10],[0,1],1)) --> [0, 4, 10]

    """
    for l in i:
        m=updatedList[l]
        pp=(2**p)
        updatedList[l]=m^pp
    return updatedList


def exponent(Ai):
    exp=0
    ans=Ai
    
    if ans==1:
        return 0
    elif ans==2:
        return 1
    else:
        while (ans>0):
            g=2**exp
            ans=Ai-g
            if (ans==1) or (ans==0):
                return(exp)   
            elif ans<0:
                return(exp-1)
            else:
                exp+=1

