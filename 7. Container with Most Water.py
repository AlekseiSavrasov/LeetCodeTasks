# SOLUTION: It works, but not optimal
# class Solution:
#     def maxArea(self, height: int) -> int:
#         new_sq_1 = 0
#         new_sq_2 = 0
#         sqs = []
#         for i, k in enumerate(height):
#             for j, l in enumerate(reversed(height)):
#                 if l < k or len(height) < j+i+1:
#                     pass
#                 else:
#                     new_sq_1 = min(k, l) * abs(len(height) - j - 1 - i)
#                     break
#             for j, l in enumerate(height):
#                 if new_sq_1 > 0 or l < k or i < j:
#                     pass
#                 else:
#                     new_sq_2 = min(k, l) * abs(i - j)
#                     break
#             sqs.append(max(new_sq_1, new_sq_2))
#         return max(sqs)
# # TEST
# s = Solution()
# print(s.maxArea([2,3,4,5,18,17,6]))


# Alternative solution (not final yet! it does not work!)
list = [2,3,4,5,18,17,6]

index = 0
s = []
for i, k in enumerate(list):
    while i > index and list[i] > list[index]:
        index = index + 1
    max_sq_1 = k * (i - index)
    s.append(max_sq_1)

index = len(list)-1  # 6
for i, k in enumerate(reversed(list)):
    while len(list)-i-1 < index and list[i] > list[index]:
        index = index - 1
    max_sq_2 = k * (index - i)
    s.append(max_sq_2)
print(max(s))