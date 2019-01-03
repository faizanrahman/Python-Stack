#Create a class called Node.This will be used to create nodes to insert into the lists.

# The class takes in one value, the value that each node will contain. By default, the next property of every node will be none(null in JS).
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# Create a class called SList. This will be used to create lists. Lists will contain nodes.

class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    def addNote(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node

    def printAllValues(self, msg=""):
        runner = self.head
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(runner.value)
            runner = runner.next
        print(runner.value)

print("==================START OF PROGRAM==============")
list = SList(5)
list.addNote(7)
list.addNote(9)
list.addNote(1)

list.printAllValues("Attempt 1")
