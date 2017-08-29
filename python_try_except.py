### Python try-except

# Ask our user for a number
print("Please enter a number!")

# Keep going until we succeed and hit `break`
while True:

    try:
    # Try to convert the user's input string to an integer
        value = int(raw_input(">> "))
        break
    
    except ValueError:
    # int() will throw a ValueError if the string couldn't be converted, e.g. if
    # the user entered a letter rather than a number. Then do this:
        print("Try again!")
        