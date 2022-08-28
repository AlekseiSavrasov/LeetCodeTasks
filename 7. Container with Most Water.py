# https://leetcode.com/problems/container-with-most-water/
# SOLUTION:
height = [1,8,6,2,5,4,8,3,7]

index_max = len(height)-1
s = []

# For each vertical line we find the one on the right side, which is higher
for i, k in enumerate(height):
    while height[index_max] < k and index_max > i:
        index_max = index_max-1
    max_sq = k*(index_max - i)
    s.append(max_sq)

# We do the same for the lines on the left side
height.reverse()
index_max = len(height)-1

for i, k in enumerate(height):
    while height[index_max] < k and index_max > i:
        index_max = index_max-1
    max_sq_r = k*(index_max - i)
    s.append(max_sq_r)

print(max(s))

# Good solution from LeetCode
# https://leetcode.com/problems/container-with-most-water/discuss/2485674/simple-python-solution
# def maxArea(self, height: List[int]) -> int:
#     r = len(height) - 1
#     l = 0
#     maxarea = 0
#     while l != r:
#         width = r - l
#         hei = min(height[r], height[l])
#         area = width * hei
#         if area > maxarea:
#             maxarea = area
#         if height[l] > height[r]:
#             r -= 1
#         else:
#             l += 1
#
#     return (maxarea)