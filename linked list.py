class Node:
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):  
    self.head = None

  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode

  def insertAfter(self,value,new_value):
    current = self.head
    while current!=None:
      if current.data==value:
        break
      current = current.next
    if(current==None):
      print("Value not found")
      return
    new_node = Node(new_value)
    new_node.next = current.next
    current.next = new_node
  
  def display(self):
    current = self.head
    while(current!=None):
      print(current.data)
      current = current.next


LL = LinkedList()
n = int(input("How many number do you want to insert in the linked List "))
while n:
  data = int(input("Enter the number to insert "))
  LL.insert(data)
  n = n-1
new_data = int(input("Enter the new value to be inserted "))
prev_data = int(input("Enter the value after which new value is to be inserted "))
LL.insertAfter(prev_data,new_data)
LL.display()