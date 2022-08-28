# https://leetcode.com/problems/3sum/

nums = [-1,0,1,2,-1,-4]
result = []

for i, k in enumerate(nums):
    for j, l in enumerate(nums):
        if i!=j and -(k+l) in nums \
                and list([k, l, -(k+l)]) not in nums\
                and list([l, k, -(k+l)]) not in nums\
                and list([k, -(k+l), l]) not in nums\
                and list([l, -(k+l), k]) not in nums \
                and list([-(k+l), k, l]) not in nums \
                and list([-(k+l), l, k]) not in nums:
            result.append(list([k,l, -(k+l)]))
print(result)