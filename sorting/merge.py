""" Simple script to perform merge sort recursively 
    on a List(array) passed to the function merge()"""

def merge(array):
    """ 
    sorts the list using merge sort algorithm
    itype: List
    rtype: List 
    """
    length=len(array)
    if length>1:
        mid=length//2
        left=merge(array[:mid])
        right=merge(array[mid:])
    else:
        return array

    l,r,k=0,0,0
    new=[]

    while l<len(left) and r < len(right):
        if left[l]<right[r]:
            new.append(left[l])
            l+=1
        else:
            new.append(right[r])
            r+=1
        k+=1
    if l<len(left):
        while l<len(left):
            new.append(left[l])
            l+=1
            k+=1
    if r<len(right):
        while r<len(right):
            new.append(right[r])
            r+=1
            k+=1
    return new



if __name__=="__main__":
    array=[ int(i) for i in input("please enter the numbers with space seperations to be sortred: ").split()]
    print("Given array: ", array)
    new=merge(array)
    print(new)