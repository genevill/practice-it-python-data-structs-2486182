from collections import namedtuple
import csv

def main():
    #add code here
    #read data/Customer.csv
    #Create workable objects with each line
    customer_tuple = []
    with open('./data/Customer.csv', "r") as csvfile:
        reader = csv.reader(csvfile)
        #for row in reader:
        #    print(row)
        Customer = namedtuple('Customer', next(reader))
        for customer in reader:
            customer_tuple.append(Customer._make(customer))

    print(customer_tuple[0])
    print(getattr(customer_tuple[0], "CustomerID"))
    #print(spamreader)
    #for emp in map(EmployeeRecord._make, csv.reader(open("Customer.csv", "rb"))):
    #    print(emp.name, emp.title)

    return

if __name__ == "__main__":
    main()