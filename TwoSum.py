# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

def twoSum(nums, target):
    res = [0, 0]
    if 2 > len(nums) > 104 or -109 > target > 109:
        return None
    for i in range(len(nums)):
        dif = target - nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == dif:
                res[0] = i
                res[1] = j
    return res


list1 = twoSum([2, 7, 11, 15], 9)
print(list1)
list2 = twoSum([3, 2, 4], 6)
print(list2)
list3 = twoSum([3, 3], 6)
print(list3)
