'''
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
After doing so, return the head of the final linked list.  You may return any such answer.

Example 1:
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted

'''
'''
Approach Using prefix sum and dictionary. Create a dummy node and append it to the head. 
Calculate prefix sum and add that pSum to the dictionary if its not there in the dictionary and its value will the current node at which it is pointing.
If prefix Sum (pSum) is already present in the dictionary that means that adding current node's value resulted in a zero value. 
So, for that we will create a start and temp variables that will begin from the d[pSum]'s value node. and we will loop until temp reaches the current node
We will also add the temp node's value to a prefix variable. We will also remove the values or nodes from the dictionary till the temp reaches curr since, we have to remove all the nodes upto the SumZero node.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        pSum = 0 
        d = dict() 

        dummy = ListNode(0)
        dummy.next = head
        d[0] = dummy 

        while(curr): 
            pSum+=curr.val
            if pSum not in d:
                d[pSum] = curr
            else:
                prefix = pSum
                start = d[pSum]
                temp = start
                while(temp!=curr):
                    temp = temp.next 
                    prefix += temp.val

                    if temp!= curr:
                        d.pop(prefix)
                start.next = temp.next

            curr = curr.next 

        return dummy.next
        

        

        