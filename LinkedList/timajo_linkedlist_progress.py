# Timajo, Kurt Vincent O.
# CpE - 2B

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
        
#Singly LinkedList
class LinkedList:
  def __init__(self):  
    pass
    
  def new(self):
    self.head = None
    self.tail = None
    return self

  def add_to_head(self, data):
    node = Node(data, self.head)
    self.head = node
    
    if node.next == None:
      node.next = self.head
  
  def add_to_tail(self, data):
    if self.head is None:
      self.head = Node(data, None)
      return

    itr = self.head
    while itr.next:
      itr = itr.next
    
    itr.next = Node(data, None)
    
  def add_before_info(self, index, data):
    if index<0 or index > self.length():
      raise Exception("Invalid index")
    
    if index == 0:
      self.add_to_head(data)
      return 
    
    count = 0
    itr = self.head
    while itr:
      if count == index -1:
        node = Node(data, itr.next)
        itr.next = node
        break
      
      itr = itr.next
      count += 1
  
  def find(self, x):
    p = self.head
    print(p)
    while p != None:
      if p.data == x:
        return True
      p = p.next
      
    return False
      
  
  def toString(self):
    if(self.head is None):
      print("Linkedlist is empty.")
      return 
    
    itr = self.head
    llstr = ''
    while itr:
      llstr+=str(itr.data) + " -> "
      itr = itr.next
    
    print(llstr)    
    
  def delete_at(self, index):
    if index<0 or index > self.length():
      raise Exception("invalid index")
    
    if index==0:
      self.head = self.head.next
      return
    
    count = 0
    itr = self.head
    while itr:
      if count == index - 1:
        itr.next = itr.next.next
        
      itr = itr.next
      count += 1
  
  def is_empty(self):
    return self.head == None
  
  def length(self):
    count = 0
    itr = self.head
    while itr:
      count+=1
      itr = itr.next
    return count
  
  
ll = LinkedList()
ll.new()
print(ll.is_empty())
ll.add_to_head(12)
ll.add_to_head(53)
ll.add_to_tail(31)
ll.add_to_tail(79)
ll.toString()
print(ll.find(11))
# ll.add_before_info(1,99)
# print(ll.is_empty())
# ll.toString()
# ll.delete_at(2)
# ll.toString()
# # print(ll.length())
# print(ll.find(78))

