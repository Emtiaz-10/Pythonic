is_weekend = True
is_holiday = False

# Nested (Harder to read)
if is_weekend:
    if is_holiday:
        print("Long Sleep")
    else:
        print("Normal Sleep")

# Flat (Cleaner)
if is_weekend and is_holiday:
    print("Long Sleep")
elif is_weekend:
    print("Normal Sleep")