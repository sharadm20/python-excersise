# Problem 1: Finding k as a sum in list

print('Enter list:')
s = input()
lst = list(map(int, s.split()))
print('Enter number whose sum to be found in List:')
k = int(input())
# Important use type conversion


def findSum(k, items=[]):
    found = False
    for i in items:
        for j in items:
            sum = j+i
            if i == j:
                continue
            if sum == k:
                found = True
                break
        if found:
            break
    return found


print(findSum(k, lst))
