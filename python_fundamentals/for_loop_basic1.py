# 1. Basic

for number in range(151):
    print(number)

# 2. Print Multiples

def printMultiples():
    for number in range(5,1000000):
        if number % 5 == 0:
            print(number)

printMultiples()
#3.Print Integers 1-100

for number in range(1,100):
    if number % 5 == 0:
        print("Coding")
        if number % 10 == 0:
            print("Dojo")
    print(number)


#4.Whoa That's Sucker huge

def oddIntegers():
    sum = 0
    for i in range(1,500000,2):
        sum = sum + i
    print(sum)

#5.Countdown by fours
for i in range(2018,0,-4):
    print(i)

#6.Flexible Conutdown

def flexibleCountdown(lowNum,highNum,mult):
    for i in range(lowNum,highNum+1):
        if i % mult == 0:
            print(i)



#Predicted Output
# 1.  3,5,1,2
# 2.  Error because list is not a integer  data type
# 3. 0,1,2,3
