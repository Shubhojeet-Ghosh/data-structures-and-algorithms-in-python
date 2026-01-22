class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        seen = set()
        while curr:
            if curr.val in seen:
                prev.next = curr.next

            else:
                seen.add(curr.val)    
                prev = curr
            
            curr = curr.next

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
    head = build_linked_list([1, 1, 2, 3, 3])
    sol = Solution()
    result = sol.deleteDuplicates(head)
    print_linked_list(result)


if __name__ == "__main__":
    main()
