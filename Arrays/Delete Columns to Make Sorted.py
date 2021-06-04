def minDeletionSize(strs):
    result = 0
    for i in range(0, len(strs[0])):
        temp = '0'
        for j in range(0, len(strs)):
            if temp > strs[j][i]:
                result += 1
                break
            else:
                temp = strs[j][i]
    print(result)
    return result


minDeletionSize(input())


"""

Sample Input = ["abc", "bce", "cae"]

"""
