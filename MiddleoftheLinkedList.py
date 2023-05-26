
# This is a single LinkedList with Fast & Slow Pointers

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:


        tempHead = head 

        while tempHead and tempHead.next: 
            head = head.next 
            tempHead = tempHead.next.next 

        return head 
    
