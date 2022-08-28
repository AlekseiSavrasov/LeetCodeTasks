# https://leetcode.com/problems/integer-to-roman/
# My solution
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {1: 'I',
                      4: 'IV',
                      5: 'V',
                      9: 'IX',
                      10: 'X',
                      40: 'XL',
                      50: 'L',
                      90: 'XC',
                      100: 'C',
                      400: 'CD',
                      500: 'D',
                      900: 'CM',
                      1000: 'M'
                      }
        result = ''

        while num != 0:
            for key in reversed(roman_dict.keys()):
                if num >= key:
                    num = num - key
                    result = result + roman_dict[key]
                    break

        return result

# Proper idea
#     def intToRoman(self, num: int) -> str:
#         pattern = [("M", 1000),
#                    ("CM", 900),
#                    ("D", 500),
#                    ("CD", 400),
#                    ("C", 100),
#                    ("XC", 90),
#                    ("L", 50),
#                    ("XL", 40),
#                    ("X", 10),
#                    ("IX", 9),
#                    ("V", 5),
#                    ("IV", 4),
#                    ("I", 1)]
#         output = ""
#         for roman, corresonding_number in pattern:
#             output += roman * (num // corresonding_number)
#             num = num % corresonding_number
#         return output