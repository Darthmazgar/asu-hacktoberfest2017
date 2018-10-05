from random import shuffle

def check(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            return False
    return True

def randSort(nums):
    sorted = check(nums)
    while not sorted:
        shuffle(nums)
        sorted = check(nums)
    return nums
