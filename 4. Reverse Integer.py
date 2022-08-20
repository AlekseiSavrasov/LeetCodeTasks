# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        length = len(str(abs(x)))
        m = abs(x)
        result = 0
        counter = 0

        for i in range(length - 1, -1, -1):
            digit = m // (10 ** i)
            print(digit)
            m = m - digit * 10 ** i
            try:
                result += 10 ** counter * digit
            except:
                result = 0
                break
            counter += 1

        if x < 0:
            result = -result

        if result < -2 ** 31 or result > 2 ** 31 - 1:
            result = 0

        return result
