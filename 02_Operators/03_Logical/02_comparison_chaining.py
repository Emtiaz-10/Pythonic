age = 25
has_license = True

# Chaining comparison
is_eligible = 18 <= age < 65

# Complex condition
can_drive = is_eligible and has_license
print(not can_drive) # False