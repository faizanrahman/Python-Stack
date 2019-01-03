#1.
x[1][0]=15;
students[0].last_name = "Bryant"
sports_directory.soccer[0] = "Andres"
z[0].y = 30

#2 
def iterateDict(arr):
    for i in range(len(arr)):
         for key,val in arr[i].items():
             print(key, " - " , val)


iterateDict([
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
])

#3

def iterateKey(arr,keyName):
    for i in range(len(arr)):
        for key,val in arr[i].items():
            if key == keyName:
                print(val)
            
iterateKey([
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
],'first_name')


#4

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def iterate(dict):
    countlocation=0
    for key, val in dojo.items():
        if key == "locations":
            countlocation=len(key)
            print(val)
            print(countlocation)
        if key == "instructors":
            print(val)
iterate(dojo)
        