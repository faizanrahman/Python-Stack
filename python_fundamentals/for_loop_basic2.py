#1. Biggie Size
def biggieSize(list):
    for i in range(len(list)):
        if(list[i] > 0):
            list[i]='big'
    return list
    
print(biggieSize([-1, "big", "big", -5]))        

#2. Count Positives

def countPositives(list):
    count=0
    for i in range(len(list)):
        if(list[i] >= 0):
            count=count + 1
    
    list[len(list) - 1]=count
    return list

print(countPositives([-1,1,1,1]))

#3.Sum Total

def sumTotal(arr):
    sum=0
    for i in range(0,len(arr)):
        sum=sum + arr[i]
    return sum
    
print(sumTotal([1,2,3,4]));


#4.Average

def average(arr):
    sum=0
    for i in range(0,len(arr)):
        sum=sum + arr[i]
    avg=sum/len(arr)
    return avg
    
print(average([1,2,3,4]))

#5. Length

def length(list):
    return len(list)
    
print(length([1,2,3,4]))


#6. Minimum 

def minimum(list):
    min=list[0]
    for i in range(0,len(list)):
        if(list[i] < min):
            min=list[i]
            
    return min
    
print(minimum([1,2,3,4]))

#7. Maximum

def maximum(list):
    max=list[0]
    for i in range(0,len(list)):
        if(list[i] > max):
            max=list[i]
            
    return max
    
print(maximum([1,2,3,4]))

#8. Ultimate Analyze

def ultimate(arr):
    sum=0
    max=arr[0]
    min=arr[0]
    
    for i in range(0,len(arr)):
        sum=sum + arr[i]
        if(arr[i] < min):
            min=arr[i]
        if(arr[i] > max):
            max=arr[i]
    avg=sum/len(arr)
    return {
        "max": max,
        "min": min,
        "sum": sum,
        "avg": avg,
        "length": len(arr)
    }
    
    
print(ultimate([1,2,3,4,5,6,7,7,8,9,10]))

#9. Reverse List

def reverseList(arr):
    for i in range(0,len(arr)/2):
        temp = arr[i]
        arr[i] = arr[len(arr) - 1 - i]
        arr[len(arr) - 1 -i] = temp
    return arr

print(reverseList([1,2,3,4,5,6]))