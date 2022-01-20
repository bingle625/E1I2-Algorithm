def sum_of(nums):
    result = []
    new_nums = {}
    for index, num in enumerate(nums):
        new_nums[num] = index
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (0-(nums[i]+nums[j])) in new_nums and new_nums[0-(nums[i]+nums[j])] > j:
                if sorted([nums[i], nums[j], 0-(nums[i]+nums[j])]) in result:
                    continue
                result.append(sorted([nums[i], nums[j], 0-(nums[i]+nums[j])]))
    print(result)


sum_of([-1, 0, 1, 2, -1, -4])
