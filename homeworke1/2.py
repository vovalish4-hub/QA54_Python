#Split Full Name

def split_name(full_name):
    return full_name.strip().split()


print(split_name(" Vova Lishtvan "))
# ["Vova", "Lishtvan"]

# My own calls
print(split_name("Olga Dai"))
# ["Olga", "Dai"]

print(split_name(" Ylia Nurlan "))
# ["Ylia", "Nurlan"]


# Simple Password Check

def check_password(password):
    return (
        len(password) >= 8
        and " " not in password
        and not password.isalpha()
    )


print(check_password("vova123"))
# True

print(check_password("vova"))
# False

print(check_password("vova 123"))
# False

# My own calls
print(check_password("Mama123"))
# True

print(check_password("qwertyu"))
# False

print(check_password("JHGFD#67"))
# True

