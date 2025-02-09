import codecs

usernames = open("usernames.txt").read().splitlines()
passwords = open("passwords.txt").read().splitlines()
idx = usernames.index("cultiris")
print(codecs.decode(passwords[idx], "rot_13"))
