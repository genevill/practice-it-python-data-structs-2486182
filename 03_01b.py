from collections import namedtuple

def main():
    Driver = namedtuple("Driver", ["Name", "Car_Type", "Capacity"])
    d = Driver("Iris", "Toyota Prius", 7)
    print(d)
    if (getattr(d, "Capacity") > 5):
        print("Capacity is enough for delivery route.")

    #add code here
    #create a driver with a name, car type, and car capacity
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    #check if they can take a certain order, given their car's capacity.
    return

if __name__ == "__main__":
    main()