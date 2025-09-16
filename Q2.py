class MyStack:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __init__(self):
        self.head=None
    def push(self, data):
        newnode=StackNode(data)
        if not self.head:
            self.head=newnode
            return self.head
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=newnode
        return self.head
    def pop(self):
        if not self.head:
            return -1
        if not self.head.next:
            val=self.head.data
            self.head=None
            return val
        curr=self.head
        while curr.next.next:
            curr=curr.next
        val=curr.next.data
        curr.next=None
        return val
