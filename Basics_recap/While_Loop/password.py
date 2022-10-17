user_name = input()
password = input()
password_match = input()
while password_match != password:
    password_match = input()
print(f"Welcome {user_name}!")