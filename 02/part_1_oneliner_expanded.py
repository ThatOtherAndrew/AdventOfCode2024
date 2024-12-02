print(sum(
    nums in (sorted(nums), sorted(nums, reverse=True))
    and all(
        1 <= abs(nums[i + 1] - nums[i]) <= 3
        for i in range(len(nums) - 1)
    )
    for nums in [
        list(map(int, line.split()))
        for line in open(0)
    ]
))
