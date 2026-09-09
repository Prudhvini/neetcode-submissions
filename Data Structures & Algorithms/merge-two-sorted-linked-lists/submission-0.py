
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        dummy =  ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val<list2.val:
                node = ListNode(list1.val)
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list2 = list2.next
            curr.next = node
            curr = node


        if list1:
            curr.next=list1
        if list2:
            curr.next=list2

        return dummy.next
