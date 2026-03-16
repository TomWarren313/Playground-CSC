name = input("Enter your full name: ")
initials = ''
for word in name.split():
    initials += word[0]
print(initials.upper())
