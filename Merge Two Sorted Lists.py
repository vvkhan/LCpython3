#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#Return the head of the merged linked list.
#Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
#NOTE: LeetCode requires implementation from the scratch, with nodes of single linked list

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        new_node = ListNode()
        cur_node = new_node

        while l1 and l2:
            if l1.val <= l2.val:
                cur_node.next = l1
                l1 = l1.next
            else:
                cur_node.next = l2
                l2 = l2.next

            cur_node = cur_node.next

        cur_node.next = l1 or l2

        return new_node.next


#Brut force
# def mergeTwoLists(list1, list2):
#     mergedList = []
#
#     if len(list1) == 0 and len(list2) == 0:
#         return mergedList
#     if len(list1) == 0 and len(list2) > 0:
#         return list2
#     if len(list1) > 0 and len(list2) == 0:
#         return list1
#
#     for i in range(len(list1)):
#         if list1[i] <= list2[i]:
#             mergedList.append(list1[i])
#             mergedList.append(list2[i])
#         else:
#             mergedList.append(list2[i])
#             mergedList.append(list1[i])
#
#     return mergedList
#
# l1 = Solution.mergeTwoLists(self, [1,2,4], [1,3,4])
# print("l1 = ", l1)
# l2 = Solution.mergeTwoLists(self, [], [])
# print("l2 = ", l2)
# l3 = Solution.mergeTwoLists(self, [], [0])
# print("l3 = ", l3)