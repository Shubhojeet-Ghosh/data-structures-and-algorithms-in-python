class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse_list(self):
        curr = self.head
        while curr:
            print(curr.data,end="->")
            curr = curr.next

        print(None)        

l1 = LinkedList()
l1.head = ListNode(10)
second = ListNode(20)
third = ListNode(30)

l1.head.next = second
second.next = third

l1.traverse_list()