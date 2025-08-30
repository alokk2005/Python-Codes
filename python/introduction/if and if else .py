# if condition :
#     do this
# else :
#     do this


height = int(input("Enter height in feet : "))

# if (height>3):
#     print("Buy Token")
#     print("Now You can board the metro")
# else:
#     print("No Token required")


if height>3:
    print("You can ride")
    age=int(input("enter your age : "))
    if age<=18:
        print("Pay 25RS")
    else:
        print("Pay 500RS")
else:
    print("You can't ride")
print("Bye")
