from collections import namedtuple
from collections import defaultdict
import csv

def getOrderData(menu_items):
    with open('./data/OrderItems.csv', "r") as csvfile:
        reader = csv.reader(csvfile)
        MenuItem = namedtuple('MenuItem', next(reader))
        for item in reader:
            if (menu_items.get(item[2], True)):
                print(item)
                menu_items[item[2]] = makeNamedTuple(item)
            else:
                print(menu_items[item[2]].Quantity + ", " + menu_items[item[3]])
                menu_items[item[2]] = menu_items[item[2]].Quantity + menu_items[item[3]]
                menu_items[item[2]] = makeNamedTuple(item)

def makeNamedTuple(item):
    menu_item = namedtuple("menu_item", ["ProductID", "Quantity"])
    return menu_item(item[2], item[3])

def main():
    #add code here
    menu_items = defaultdict(set)

    getOrderData(menu_items)
    
    print(menu_items)
    print(menu_items["ENT001"])
    print(menu_items["ENT001"].ProductID)

    return

if __name__ == "__main__":
    main()