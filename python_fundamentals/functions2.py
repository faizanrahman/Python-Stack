#1. Countdown
def countdown(num):
    list1=[];
    for i in range(num,-1,-1):
        
        list1.append(i)
    return list1
    

#2. Print and Return
def printReturn(list):
    print(list[0])
    return list[1]



#3. First Plus Length

def firstLength(list):
    return (list[0] + len(list)

#4.Values greater than second

def greaterThanSecond(arr):
    count = 0
    arr1=[]
    for i in range(0,len(arr)):
        if(arr[i] > arr[1]):
            arr1.append(arr[i])
            count=count + 1
    return arr1
    
print(greaterThanSecond([2,4,5,6,7,1]))



#5. This Length, That Value

def length(size, value):
    list=[]
    for i in range(0,size):
        list.append(value)        
    return list
