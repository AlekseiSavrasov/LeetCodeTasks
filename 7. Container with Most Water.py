# SOLUTION: It works, but not optimal
class Solution:
    def maxArea(self, height: int) -> int:
        new_sq_1 = 0
        new_sq_2 = 0
        sqs = []
        for i, k in enumerate(height):
            for j, l in enumerate(reversed(height)):
                if l >= k and j+1 != len(height) - i:
                    new_sq_1 = min(k, l) * abs(len(height) - j - 1 - i)
                    break
                else:
                    pass
            for j, l in enumerate(height):
                if l >= k and i != j:
                    new_sq_2 = min(k, l) * abs(i - j)
                    break
                else:
                    pass
            sqs.append(max(new_sq_1, new_sq_2))
        return max(sqs)
# TEST
s = Solution()
print(s.maxArea([1, 0, 0, 0, 0, 0, 0, 7, 8]))