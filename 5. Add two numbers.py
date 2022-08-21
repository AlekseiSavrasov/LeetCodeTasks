# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Add a class of list to make the operations understandable
class LinkedList:
    def __init__(self):
        self.head = None # a head is the current node with its value and link

    def insert(self, data): # insert a value to the end of list
        newNode = ListNode(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self): # Print all values from the list one by one
        current = self.head
        while(current):
            print(current.val)
            current = current.next

    def list_length(self): # Estimate length of the list
        length = 0
        current = self.head
        while(current):
            length += 1
            current = current.next
        return length

class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    # Add a class of list to make the operations understandable
    class LinkedList:
        def __init__(self):
            self.head = None  # a head is the current node with its value and link

        def insert(self, data):  # insert a value to the end of list
            newNode = ListNode(data)
            if (self.head):
                current = self.head
                while (current.next):
                    current = current.next
                current.next = newNode
            else:
                self.head = newNode

        def printLL(self):  # Print all values from the list one by one
            current = self.head
            while (current):
                print(current.val)
                current = current.next

        def list_length(self):  # Estimate length of the list
            length = 0
            current = self.head
            while (current):
                length += 1
                current = current.next
            return length


    def addTwoNumbers(self, l1: LinkedList, l2: LinkedList) -> LinkedList:
        if l1.list_length() > l2.list_length():
            add = l1.list_length() - l2.list_length()
            for i in range(add):
                l2.insert(0)
        else:
            add = l2.list_length() - l1.list_length()
            for i in range(add):
                l1.insert(0)

        current_l1 = l1.head
        current_l2 = l2.head
        l3 = LinkedList()
        extra_num = 0

        for i in range(l1.list_length()):
            if current_l1.val + current_l2.val + extra_num >= 10:
                l3.insert((current_l1.val + current_l2.val + extra_num) % 10)
                extra_num +=1
                current_l1 = current_l1.next
                current_l2 = current_l2.next
            else:
                l3.insert(current_l1.val + current_l2.val + extra_num)
                extra_num = 0
                current_l1 = current_l1.next
                current_l2 = current_l2.next
        return l3

# Example lists to test the result
# # l1: 123
# l1 = LinkedList()
# l1.insert(1)
# l1.insert(2)
# l1.insert(3)
#
# # l2: 77
# l2 = LinkedList()
# l2.insert(1)
# l2.insert(0)
#
# s = Solution()
# result = s.addTwoNumbers(l1, l2)
# result.printLL()

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode):
#         return l1.val

# print(s.addTwoNumbers(l1, l2))

#         if len(l1) > len(l2):
#             add = len(l1) - len(l2)
#             l2 = l2 + [0] * add
#         else:
#             add = len(l2) - len(l1)
#             l1 = l1 + [0] * add
#
#         counter = 0
#         l3 = [0] * len(l1)
#         for i in range(len(l1)):
#             if l1[i] + l2[i] + counter >= 10:
#                 l3[i] = (l1[i] + l2[i] + counter) % 10
#                 counter += 1
#             else:
#                 l3[i] = l1[i] + l2[i] + counter
#                 counter = 0
#         return l3
#
# s = Solution()
# print(s.addTwoNumbers([1, 2, 3, 4], [5, 3, 1]))