# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop through both lists
        while l1 or l2 or carry:
            # Get the values from the current nodes or 0 if any list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
            
            # Add the new value as a node to the result list
            current.next = ListNode(new_val)
            current = current.next
            
            # Move to the next nodes in l1 and l2 if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the next of dummy head, which points to the actual start of the result list
        return dummy_head.next