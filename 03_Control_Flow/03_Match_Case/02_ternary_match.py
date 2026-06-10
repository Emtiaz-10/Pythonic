def check(is_admin):
    match is_admin:
        case "yes"|"y"|"1": return True
        case "no"|"0" : return False
        case _:
            print("invalid")
            return False
is_admin = check(input("Do u admin?").lower().strip())
#is_admin = True if input("Do u admin? : ").strip().lower() == "yes" and "y" else False

status = "granted" if is_admin else "denied"
print(status)

if is_admin:
    print("hi")
if not is_admin:
    print("hey")