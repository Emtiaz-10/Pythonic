nums = [1, 2, 3]   #old loc

other = nums
nums.append(4)
print(other)

print("reassignment")
nums = [3,4]    # loc changed
print(nums,other)

# -----------------------------------#

n = [1, 2, 3]   #old loc

o = n
print("Mutation")
n.clear()
n.extend([8,9])
print(n,o)