# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Node:
    def __init__(self, data):
        self.data =  data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False
            
    def ListLength(self):
        currentNode  = self.head
        length = 0
        
        while currentNode is not None:
            length+=1
            currentNode =  currentNode.next
        return length
        
        
    def insertAtEnd(self, newNode):
        # head-> John-> None
        if self.head is None:
            self.head = newNode
        else:
             # head->John->Versha -> None
            lastNode =  self.head
            while True:
                if lastNode.next is None:
                    break
                else:
                    lastNode = lastNode.next
            lastNode.next = newNode
            
    def insertAtBegin(self, newNode):
        ## store the current head node in the temp node
        # make the new node as head node
        # make the next of your newnode point to temp node
        
        if self.head is None:
            self.head  = newNode
            
        else:
            # head->John->Versha ->None
            temp = self.head
            self.head = newNode
            self.head.next = temp
            del temp
            
    def insertAtPos(self, pos, newNode):
        # traverse till the  given position
        # store the details of previous node in a temp node
        # make a connection from next of previous node to new node
        # make a connection from next of new node to a node at a given position 
        if pos == 0:
            self.insertAtBegin(newNode)
            return
        
        currentNode = self.head
        currentPosition = 0
        
        while True:
            if currentPosition == pos:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            
            else:
                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition+=1
        
    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head  = self.head.next
            previousHead.next = None
            
        else:
            print("Linked list is Empty, deletion failed")
            
    def deleteEnd(self):
        #traverse till the end of the list
        #preserve the second last node in a temporary node
        #delete the last node
        #make the nest of the temporary node to None
        lastNode =  self.head
            
        while lastNode.next is not None:
            previousNode =  lastNode
            lastNode = lastNode.next
            
        previousNode.next  = None
        
    def deleteAtPos(self, pos):
        #Traverse till the node which you want to delete
        #Preserve the details of the previous node
        # make a connection from next of the previous node to the next of the node
        if pos<0 or pos>= self.listLength():
            print("pos is invalid")
            
        if self.isListEmpty() is False:
            if pos == 0:
                self.deleteHead()
                return
                
            currentNode = self.head
            currentPosition = 0
            
            while True:
                if currentPosition == pos:
                    previousNode.next = currentNode.next
                    currentNode.next  = None
                    break
                
                else:
                    previousNode = currentNode
                    currentNode = currentNode.next
                    currentPosition+=1
                    
    def printNode(self):
        if self.head is None:
            print("List is Empty")
            
        currentNode = self.head
        
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
            
        

firstNode = Node("John")
thirdNode = Node("Bay")
LL = LinkedList()
LL.insertAtEnd(firstNode)
LL.insertAtEnd(thirdNode)
secondNode = Node("Versha")
LL.insertAtBegin(secondNode)
fourthNode = Node("brian")
#LL.insertAtPos(0,fourthNode)
LL.printNode()
#LL.deleteEnd()
#LL.deleteAtPos(1)
LL.deleteHead()
LL.printNode()