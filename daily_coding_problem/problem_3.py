"""Given an array of integers,
find the first missing positive integer in linear time and constant space.
In other words,
find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3."""


def diffOfNum(num1, num2):
    return num1-num2


print('Enter array of numbers:')
s = input()
arr = list(map(int, s.split()))
sortedArr = sorted(arr)
leng = len(sortedArr)
num = None
j = 0
for i in range(leng):
    if j < leng - 1:
        j = i + 1
    if sortedArr[i] >= 0:
        if diffOfNum(sortedArr[j], sortedArr[i]) >= 2:
            num = sortedArr[i] + 1
        else:
            num = sortedArr[i] + 1

print(num)
