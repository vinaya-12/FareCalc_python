

rates = {'Economy': 10,'Premium': 18,'SUV': 25}
def calculate_fare(km, vehicle_type, hour):
    
    base_rate = rates[vehicle_type]
    total = km * base_rate

    if 17 <= hour <= 20:
        total *= 1.5

    return total


while True:
    try:
        print("\n=== CityCab Fare Calculator ===")

        vehicle = input("Enter Vehicle Type (Economy/Premium/SUV) or Exit: ")


        if vehicle.lower() == "exit":
            break
        if vehicle not in rates:
            raise ValueError("Service Not Available")
        km = float(input("Enter Distance (km): "))

        if km <= 0:
            raise ValueError("Distance must be greater than 0")

        hour = int(input("Enter Hour of Travel (0-23): "))

        if hour < 0 or hour > 23:
            raise ValueError("Hour must be between 0 and 23")

        fare = calculate_fare(km, vehicle, hour)

        print("\n----- PRICE RECEIPT -----")
        print("Vehicle Type   :", vehicle)
        print("Distance       :", km, "km")
        print("Travel Hour    :", hour)

        if 17 <= hour <= 20:
            print("Surge Applied  : Yes (1.5x)")
        else:
            print("Surge Applied  : No")

        print("Final Fare     : Rs.", round(fare, 2))
        
    except ValueError as e:
        print(" Error:", e)

    except Exception:
        print("Invalid input")