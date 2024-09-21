# Multiple If

print("Welcome to the rollercoaster!")

height = int(input("How tall are you? (inches)\n"))
allowed_height = 50
bill = 0

if height >= allowed_height:
    print("You can ride the rollercoaster.")
    age = int(input("How old are you?\n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age < 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age > 55:
        bill = 5
        print("Elderly tickets are $5.")
    else:
        bill = 12
        print("Adult tickets are $12")
    
    want_photo = input("Do you want a photo? Y or N")
    if want_photo = Y:
        bill += 3 # adds 3 to the value of the variable 'bill'. += is the same as: bill = bill + 3
    
    print(f"Please pay ${bill}")
else:
    print(f"Sorry. You must be {allowed_height} inches tall to ride.")