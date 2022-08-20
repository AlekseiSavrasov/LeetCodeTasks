class Solution:
    def romanToInt(self, s: str):
        result = 0 # Записываем итог
        m = 0 # Кладём в память предыдущий символ после каждой итерации

        for i in s[::-1]:
            if i == 'I':
                a = 1
            elif i == 'V':
                a = 5
            elif i == 'X':
                a = 10
            elif i == 'L':
                a = 50
            elif i == 'C':
                a = 100
            elif i == 'D':
                a = 500
            elif i == 'M':
                a = 1000

            if a >= m:
                result += a
            else:
                result -= a
            m = a
        return result

# Test
s = Solution()
result = s.romanToInt('MCMXCIV')
print(result)