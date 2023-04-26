def find_duplicate(nums):
    for num in nums:
        if type(num) != int or num < 0:
            return False

    nums.sort()

    for index in range(len(nums) - 1):
        if nums[index] == nums[index + 1]:
            return nums[index]

    return False
