# SOLUTION: It works, but not optimal
class Solution:
    def maxArea(self, height: int) -> int:
        new_sq_1 = 0
        new_sq_2 = 0
        sqs = []
        for i, k in enumerate(height):
            for j, l in enumerate(reversed(height)):
                if l < k or len(height) < j+i+1:
                    pass
                else:
                    new_sq_1 = min(k, l) * abs(len(height) - j - 1 - i)
                    break
            for j, l in enumerate(height):
                if l < k or i < j:
                    pass
                else:
                    print('Вхят i: ' + str(i) + ' k: ' + str(k) + ' j: ' + str(j) + ' l: ' + str(l))
                    new_sq_2 = min(k, l) * abs(i - j)
                    break
            sqs.append(max(new_sq_1, new_sq_2))
        return max(sqs)
# TEST
s = Solution()
print(s.maxArea([2,3,4,5,18,17,6]))


i = 4
k = 18

j = 1
l = 17