# HolidayCost = take # of nights, city, and # of days then print it all out
# resubmitting to address feedback. so much easier after banging my head on
# tic tac toe! :)


def holiday_cost(nights, days, city):
    total_hotel = nights * 50
    total_rental = days * 10
    if city is 'Chicago':
        total_air = 200
    elif city is 'Sydney':
        total_air = 1000
    elif city is 'Morocco':
        total_air = 1200
    print("Total cost: $", (total_hotel + total_rental + total_air))


holiday_cost(3, 4, 'Chicago')
