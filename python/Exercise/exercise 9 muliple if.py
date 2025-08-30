height=int(input("Enter your height : "))
bill=0

if height>=3:
    print("you can ride")
    age=int(input("Enter you age : "))
    if age<12:
        bill=150
        print("Ticket price is 150 Rs.")
    elif age<=18:
        bill=250
        print("Ticket price is 250 Rs.")
    else:
        bill=500
        print("Ticket price is 500 Rs.")

    want_photo=input("Do you want to take photo(Yes/No) : ")
    if want_photo == 'Yes' or want_photo == 'yes':
        bill+=50
    
    print(f"Your total bill is : {bill}")

else:
    print("you can't ride")
print("Thank you. Enjoy the Ride.")
