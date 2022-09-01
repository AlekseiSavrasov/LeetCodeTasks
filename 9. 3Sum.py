# https://leetcode.com/problems/3sum/

nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
result = []

plus = []
minus = []
zero = []

# Split numbers
for i in nums:
    if i == 0:
        zero.append(i)
    elif i < 0:
        minus.append(i)
    else:
        plus.append(i)

# Special case with zeros
if len(zero) >= 3:
    result.append([0, 0, 0])
if len(zero) >= 1:
    for i in plus:
        if -i in minus and [0, i, -i] not in result:
            result.append([0, i, -i])

# Other cases
for i, k in enumerate(plus):
    for j, l in enumerate(plus):
        if i != j and -k-l in minus \
                and [k, l, -k-l] not in result \
                and [l, k, -k-l] not in result:
            result.append([k, l, -k-l])
for i, k in enumerate(minus):
    for j, l in enumerate(minus):
        if i != j and -k-l in plus \
                and [k, l, -k-l] not in result \
                and [l, k, -k-l] not in result:
            result.append([k, l, -k-l])
print(result)


# for i, k in enumerate(nums):
#     for j, l in enumerate(nums):
#         if i!=j and -(k+l) in nums \
#                 and list([k, l, -(k+l)]) not in nums\
#                 and list([l, k, -(k+l)]) not in nums\
#                 and list([k, -(k+l), l]) not in nums\
#                 and list([l, -(k+l), k]) not in nums \
#                 and list([-(k+l), k, l]) not in nums \
#                 and list([-(k+l), l, k]) not in nums:
#             result.append(list([k,l, -(k+l)]))
# print(result)