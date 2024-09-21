# Elif

# elif is used to add other conditions to an if / else statement.
# elif works because the condition is ran first through the if statement
# then all the elifs in order from top to bottom
# the through the else


print("Welcome to the rollercoaster!")

height = int(input("How tall are you? (inches)\n"))
allowed_height = 50

if height >= allowed_height:
    print("You can ride the rollercoaster.")
    age = int(input("How old are you?\n"))
    if age < 12:
        print("Please pay $5.")
    elif age < 18:
        print("Please pay $7.")
    elif age > 55:
        print("Please pay $5.")
    else:
        print("Please pay $12")
else:
    print(f"Sorry. You must be {allowed_height} inches tall to ride.")