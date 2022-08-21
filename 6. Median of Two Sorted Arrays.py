# SOLUTION
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums3 = sorted(nums1 + nums2)
        if len(nums3) % 2 == 0:
            median = (nums3[int(len(nums3)/2)] + nums3[int(len(nums3)/2-1)])/2
        else:
            median = nums3[int(len(nums3)//2)]
        return float(median)


# TEST
s = Solution()
res = s.findMedianSortedArrays([1, 3], [2, 3, 4])
print(res)