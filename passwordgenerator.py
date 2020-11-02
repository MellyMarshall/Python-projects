import random, string
password_length = int(input("choose any length for your password. remember that we need this in numbers."))
password_characters = string.ascii_letters + string.digits + string.punctuation
password = []
for x in range(password_length):
    password.append(random.choice(password_characters))
print(''.join(password))