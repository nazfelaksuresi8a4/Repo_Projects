class LinkedList(object):
    def __init__(self,value=None,addr=None):
        self.value = value
        self.addr = addr

list_1 = LinkedList(1,LinkedList(2,LinkedList(3)))

print(list_1.addr.value)
