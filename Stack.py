class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Stack:
    def __init__(self):
        self.head=None

    def insert(self,data):
        Newnode=Node(data)
        if(self.head):
            current=self.head
            self.head=Newnode
            self.head.next=current
        else:
            self.head=Newnode        

    def printstack(self):
        current=self.head
        while(current):
            print(current.data)
            current=current.next

no_of_nodes=int(input("Enter no of nodes::"))
St=Stack()
while(no_of_nodes):
    value=int(input("Enter value to stack::"))
    St.insert(value)
    no_of_nodes=no_of_nodes-1
St.printstack()