""" This script implements quick sort algorithm recursively 
    to sort the elements in a list
"""
def quick(array):
    """ implements quick sort alogrithm
        itype:list
        rtype:list
    """
    if len(array)<=1:
        return array
    else:
        pivot=array[0]
        lp=1
        up=len(array)-1
        while lp<len(array)-1 and array[lp]<pivot:
            lp+=1
        while lp<=up:
            if array[up]<=pivot:
                temp=array[up]
                array[up]=array[lp]
                array[lp]=temp
                lp+=1
            up-=1
        #print(array[1:lp],array[lp:],pivot)
        left=quick(array[1:lp])
        right=quick(array[lp:])
        new=[]
        #print(left,right,pivot)
        new.extend(left)
        new.append(array[0])
        new.extend(right)
        return new

if __name__ == "__main__":
    array=[ int(i) for i in input("please enter the numbers with space seperations to be sortred: ").split()]
    print("Given array: ", array)
    new=quick(array)
    print(new)

""" to do in_place and iterative"""
