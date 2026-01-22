class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next

            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next
            
        tail.next = l1 if l1 else l2

        return dummy.next




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
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])

    sol = Solution()
    result = sol.mergeTwoLists(l1, l2)

    print_linked_list(result)


if __name__ == "__main__":
    main()
