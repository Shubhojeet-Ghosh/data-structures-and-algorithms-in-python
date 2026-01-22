class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        curr = head
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head = prev
        return head
    
def build_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


def main():
    head = build_linked_list([1, 2, 3, 4, 5])
    sol = Solution()
    
    print_linked_list(head)
    reversed_head = sol.reverseList(head)
    print_linked_list(reversed_head)


if __name__ == "__main__":
    main()
