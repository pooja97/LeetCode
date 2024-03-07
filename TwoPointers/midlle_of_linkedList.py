# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
first solution uses 2 pass 1 to calculate the length of the list and find the mid index. 
second pass uses 2 pointers to loop till the mid point and return the middle of the LinkedList
Run time: O(n)+O(n//2) = O(n)
space Complexity: O(1)

Second Solution uses two pointers slow and fast. 
when the fast pointer will reach the end of the list aur slow pointer will be at the middle of the list.
'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr = head
        # l = 0 
        # while(curr):
        #     l+=1 
        #     curr = curr.next

        # mid = l//2
        # if mid == 0:
        #     return head

        # prev = None 
        # curr = head 

        # while(mid>0):
        #     prev = curr
        #     curr = curr.next 
        #     mid-=1
        # prev.next = None 
        # return curr
 
        
        slow, fast = head, head 
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next 

        return slow
        