from datetime import datetime
import locale

print("Hotel Reservation Program\n")

again = "y"
while again.lower() == "y":
    # Arrival date
    while True:
        date_str = input("Enter arrival date (YYYY-MM-DD): ")
        try:
            arrival_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("This is an invalid date format. Please try again.")
            print()
            continue

        #Arrival date is less than today error
        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        if arrival_date < today:
            print("Your arrival date must be today or later. Please try again.")
            print()
        else:
            break

    # Departure date
    while True:
        date_str = input("Enter departure date (YYYY-MM-DD): ")
        try:
            departure_date = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print("This is an invalid date format. Please try again.")
            print()
            continue

        # Departure date must be after arrival date error 
        if departure_date <= arrival_date:
            print("The Departure date must be after the arrival date. Please try again.")
            print()
        else:
            break

    print()

    # calculate cost
    rate = 85.0
    rate_message = ""
    if arrival_date.month == 8:   #August high season
        rate = 105.0
        rate_message = "(High rate season)" #August high season rate message
    total_nights = (departure_date - arrival_date).days
    total_cost = rate * total_nights

    # results
    date_format = "%B %d, %Y"
    locale.setlocale(locale.LC_ALL, "en_us")
    print(f"Arrival Date:     {arrival_date:{date_format}}")
    print(f"Departure Date:   {departure_date:{date_format}}")
    print(f"Nightly rate:     {locale.currency(rate)} {rate_message}") #August high season rate message
    print(f"Total nights:     {total_nights}")
    print(f"Total price:      {locale.currency(total_cost)}")
    print()

    again = input("Would you like to continue? (y/n): ")
    print()

print("Goodbye")


                                              