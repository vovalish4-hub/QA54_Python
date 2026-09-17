#Clean a Name

def clean_name(name):
    return name.strip().title()


print(clean_name("Olga Pupkina"))

print(clean_name("Masha Dai"))

#Normalize an Email

def normalize_email(email):
    return email.strip().lower()


print(normalize_email("Olgapup@outluc.com"))

#Check a File Name

def is_python_file(filename):
    return filename.lower().endswith(".py")


print(is_python_file("lesson.py"))
# True

print(is_python_file("HOMEWORK.PY"))
# True

print(is_python_file("notes.txt"))
# False

#Replace Words

def fix_message(message):
    return message.replace("bad", "good")


message = "bad weather, bad mood"

result = fix_message(message)

print(result)
# good weather, good mood

print(message)
# bad weather, bad mood

#Count a Letter

def count_letter(text, letter):
    return text.lower().count(letter.lower())


print(count_letter("Programming", "g"))
# 2

print(count_letter("Mississippi", "I"))
# 4
#Create a Short Login

def create_login(first_name, last_name):
    return first_name.strip().lower() + "." + last_name.strip().lower()


print(create_login(" Olga ", " Pupkina"))
# olga.pupkina