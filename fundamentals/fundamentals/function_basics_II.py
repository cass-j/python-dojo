# Countdown
def countDown(num):
    downList = []
    while num >= 0:
        downList.append(num)
        num -= 1
    print(downList)
    return downList

countDown(20)


# Print and Return
def printReturn(arr):
    print(arr[0])
    return arr[1]

print(printReturn([5,2]))


# First Plus Length
def firstPlusLen(arr):
    total = arr[0] + len(arr)
    return total

print(firstPlusLen([1,2,3,4,5]))


# Values Greater than Second
def greaterThanSecond(arr):
    print(len(arr))
    if len(arr) < 2:
        return False

    second = arr[1]
    greater = []
    for num in arr:
        if num > second:
            greater.append(num)
    return greater

print(greaterThanSecond([1,3,15,4,2,27,8]))


# This Length, That Value
def thisLenValue(size,value):
    arr = []
    while size > 0:
        arr.append(value)
        size -= 1
    return arr

print(thisLenValue(5,10))