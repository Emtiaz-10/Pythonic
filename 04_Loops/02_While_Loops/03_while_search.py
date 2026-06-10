target = 7
nums = [1, 3, 7, 4, 2]
idx = 0

while idx < len(nums):
    if nums[idx] == target:
        print("Found at", idx)
        break
    idx += 1



