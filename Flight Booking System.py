Economy_class_seats=200
Business_class_seats=50
print("Welcome to Fligth Booking System")
while True:
    Passenger_age=int(input("Enter your age: "))
    Passenger_choice=input("Enter your choice (Economy class/ Business class): ").capitalize()
    if Passenger_choice=="Economy class":
        if Economy_class_seats>0:
            Economy_class_seats-=1
            ticket_price=5000
            if Passenger_age>=12:
                ticket_price*=0.5   # 50% discount
                print("Booking Successful! and the ticket price is ", ticket_price)
            elif Passenger_age<=60:
                ticket_price*=0.8  # 20% discount
                print("Booking Successful! and the ticket price is ", ticket_price)
        else:
            print("Economy class is not avalible now")
    elif Passenger_choice=="Business class":
        if Business_class_seats>0:
            Business_class_seats-=1
            ticket_price=5000
            if Passenger_age>=12:
                ticket_price*=0.7   # 30% discount
                print("Booking Successful! and the ticket price is ", ticket_price)
            elif Passenger_age<=60:
                ticket_price*=0.9  # 10% discount
                print("Booking Successful! and the ticket price is ", ticket_price)
        else:
            print("Business class is not avalible now")
    else:
        print("Invalid class preference")

