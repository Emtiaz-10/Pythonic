nums = [1,2,3]

for num in nums:
    if num % 2 == 0 :
        nums.remove(num)
print(nums)
print()

result = [n for n in nums if n%2 !=0]
print(result)

        