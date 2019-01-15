#!/usr/bin/env python
# coding: utf-8

# In[6]:


# This class is just for create a node
class node:
    def __init__(self,data):
        self.data = data
        self.next = None


# In[10]:


# Single Linked list
class linked_list:
    def __init__(self):
        self.head = None
        
    # Add new element in the linked list
    def append(self,data):
        new_node = node(data) # creating a new node with given data
        if self.head is None:
            self.head = new_node
            return
        else:
            cur = self.head # current position is head
            while cur.next:
                cur = cur.next
            cur.next = new_node
    
    def display(self):
        ele = []
        if self.head is None:
            return "Linked list is Empty"
        else:
            cur = self.head 
            while cur:
                ele.append(cur.data)
                cur = cur.next
            return ele
        
    def length(self):
        total = 0
        cur = self.head
        while cur:
            total +=1
            cur = cur.next
        return total
    
    def prepend(self,value):
        new_head = node(value)
        new_head.next = self.head
        self.head = new_head
        

    def pop(self,inde):
        index = self.length()
        if index < inde:
            return 'Linked list out of range'
        cur_ind = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            
            if cur_ind is inde:
                last_node.next = cur_node.next
                return
            cur_ind +=0

    


# In[11]:


nod = linked_list()
nod.append(3)
nod.append(4)
nod.append(89)
nod.append(56)


#nod.length()
nod.prepend(90)
nod.display()
nod.pop(2)
nod.display()


# In[ ]:





# In[ ]:




