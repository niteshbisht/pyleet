# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class DeleteDuplicatesSorted:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

if __name__ == '__main__':
    dlt_duplicates_sorted = DeleteDuplicatesSorted()
    v1 = ListNode(1, None)
    v2 = ListNode(1, None)
    v1.next = v2

    v3 = ListNode(1, None)
    v2.next = v3

    res = dlt_duplicates_sorted.deleteDuplicates(v1)
    print(res)