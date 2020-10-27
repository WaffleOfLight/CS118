import random
def bubSort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
    return nums


lst = []
for i in range(random.randint(5, 10)):
    lst.append(random.randint(1, 20))
print("This is the list before bubble sorting: ")
print(lst)
arr = bubSort(lst)
print("This is the list after bubble sorting: ")
print(lst)