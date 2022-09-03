def letterCombinations(digits: str) -> str:
    keys = {'2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}
    start = [x for x in keys[digits[0]]]
    result_c = []

    for i in digits[1:]:
        if i == '1':
            continue
        else:
            for j in start:
                for k in keys[i]:
                    result_c.append(j + k)
            start = result_c

    return result_c

print(letterCombinations('123'))