# Nested if else condition

# you can 'nest' and if/else within an if/else

print("Welcome to the rollercoaster!")

height = int(input("How tall are you? (inches)\n"))
allowed_height = 50

if height >= allowed_height:
    print("You can ride the rollercoaster.")
    age = int(input("How old are you?\n"))
    if age < 18:
        print("Please pay $7.")
    else:
        print("Please pay $12")
else:
    print(f"Sorry. You must be {allowed_height} inches tall to ride.")