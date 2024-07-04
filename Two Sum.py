nums = [1,2,3,4,5,6,7,8,9]
def twoSum (nums, target):
    for i in range(len(nums)):
        complement = target - nums[i]
        index = nums.index(complement)
        return (index, i)

      

print(twoSum(nums, 6))