class Node:
  def __init__(self, data=None, next=None):
    self.data = data 
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_begining(self, data):
    node = Node(data, self.head)
    self.head = node

  def insert_at_end(self, data):
    node = Node(data, None)
    if self.head is None:
      self.head = node
      return

    itr = self.head

    while itr.next is not None:
      itr = itr.next

    itr.next = node

  def insert_values(self, data_list):
    self.head = None

    for data in data_list:
      self.insert_at_end(data)

  def insert_after_value(self, value, data):
    itr = self.head
   
    while itr:
      if itr.data == value:
        node = Node(data, itr.next)
        itr.next = node
      #   itr.next = itr.next.next
      #   return
      itr = itr.next

  def insert_at(self, index, data):
    if index < 0 or index > self.get_length():
      print("the index is not valid")
      return

    if index == 0:
      self.head = Node(data, self.head)
      return 

    tracker = 0
    itr = self.head

    while itr:
      if tracker == index - 1:
        new_node = Node(data, itr.next)
        itr.next = new_node

      tracker += 1
      itr = itr.next
        
  def remove_at(self, index):
    if index < 0 or index >= self.get_length():
      print("the index is not valid")
      return

    if index == 0:
      self.head = self.head.next

    tracker = 0
    itr = self.head

    while itr:
      if tracker == index - 1:
        itr.next = itr.next.next
        return

      itr = itr.next
      tracker += 1

  def remove_by_value(self, value):
    itr = self.head

    if value == itr.data:
      self.head = self.head.next

    
    while itr.next is not None:
      if itr.next.data == value:
        itr.next = itr.next.next
        return
      itr = itr.next

  def get_length(self):
    length = 0
    itr = self.head

    while itr:
      length += 1
      itr = itr.next

    return length

  def print(self):
    if self.head is None:
      print("linked list is empty")
      return

    itr = self.head
    llstr = ""

    while itr:
      llstr += str(itr.data) + "---> "
      itr = itr.next

    print(llstr)

ll = LinkedList()
# ll.insert_at_begining(89)
# ll.insert_atdef insert_at_end(5)
ll.insert_values(["1", "2", "3", "4", "5"])
ll.print()
# ll.remove_by_value("1")
ll.insert_after_value("5", "99")
# ll.remove_at(2)
# ll.get_length()
ll.print()