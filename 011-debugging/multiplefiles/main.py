import myfile

print("What's going on MAIN ?")

try:
    myfile.get_user_age()
except ValueError:
    print("That's not a valid value for your age!")