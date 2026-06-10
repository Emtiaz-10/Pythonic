name = ""           # empty string or array indicates false
default = "Guest"

# The 'or' trick
user = name or default
print(user)  # "Guest"

# Short-circuiting safety
nums = [-2]
if nums and nums[0] > 0:
    print("First is positive")