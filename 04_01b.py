from collections import namedtuple
from collections import defaultdict

def main():
    Food = namedtuple("Food", ["identifier", "name"])

    nadias_list = [
        Food("STA001",  "Panko Stuffed Mushrooms"),
        Food("BEV003",	"Cafe Latte"),
        Food("STA002",	"Mini Cheeseburgers"),
        Food("STA003",	"French Onion Soup"),
        Food("STA004",	"Artichokes with Garlic Aioli"),
        Food("STA005",	"Parmesan Deviled Eggs"),
        Food("SAL001",	"Garden Buffet"),
        Food("SAL002",	"House Salad"),
        Food("SAL003",	"Chefs Salad"),
        Food("SAL004",	"Quinoa Salmon Salad"),
        Food("ENT001",	"Classic Burger"),
        Food("ENT002",	"Tomato Bruschetta Tortellini"),
        Food("ENT003",	"Handcrafted Pizza"),
        Food("ENT004",	"Barbecued Tofu Skewers"),
        Food("ENT005",	"Fiesta Family Platter"),
        Food("DES001",	"Creme Brulee"),
        Food("ENT001",	"Classic Burger"),
        Food("DES002",	"Cheesecake"),
        Food("DES003",	"Chocolate Chip Brownie"),
        Food("DES004",	"Apple Pie"),
        Food("STA001",	"Panko Stuffed Mushrooms"),
        Food("DES005",	"Mixed Berry Tart"),
        Food("DES005",	"Mixed Berry Tart"),
        Food("BEV001",	"Tropical Blue Smoothie"),
        Food("BEV002",	"Pomegranate Iced Tea"),
        Food("DES005",	"Mixed Berry Tart"),
        Food("BEV003",	"Cafe Latte"),
        Food("DES005",	"Mixed Berry Tart"),
        Food("BEV003",	"Cafe Latte"),
    ]

    menu = defaultdict(set)
    #entree, salad, starter, dessert
    #use a set as the default value
    for item in nadias_list:
        if ("ENT" in item.identifier[0:3]):
            menu["Entree"].add(item)
        if ("SAL" in item.identifier[0:3]):
            menu["Salad"].add(item)
        if ("STA" in item.identifier[0:3]):
            menu["Starter"].add(item)
        if ("DES" in item.identifier[0:3]):
            menu["Dessert"].add(item)
    print(menu)
    return

if __name__ == "__main__":
    main()