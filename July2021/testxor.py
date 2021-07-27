ind=[]
l=[3,7,10]
k=2

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
    
def checkodd(l):
    for i in range(len(l)):
        if l[i]%2==1:
            ind.append(i)
    return(ind)


def convertodd():
    i1=checkodd(l)
    if len(i1)<=k:
        print(xor(l,ind,0))

convertodd()
