# manager module
menu = {}
orders = []

#......................Menu Functions.......................................
def add_or_update_menu():
    item_id = input("Enter item id: ")
    name = input("Enter item name : ")
    price = float(input("Enter price: "))

    menu[item_id] = {"name" : name, "price" : price}
    print("menu Updated! successfully...\n")

def display_menu():
    print("\n........MENU........")
    for item_id, details in menu.items():
     print(f"{item_id}: {details['name']} - $ {details['price']}")
     print()

#.........................ORDER FUNCTIONS.....................................

def place_order():
    order_id = input("Enter order id: ")
    date = input("Enter Date (YYY-MM-DD): ") 

    order_items = []
    total = 0

    while True:
        display_menu()  
        item_id = input("Enter item id (or 'done'): ") 
        if item_id.lower() == "done":
            break
        if item_id in menu:
            qty = int(input("Enter Quantity: "))
            price = menu[item_id]["price"]*qty

            order_items.append
            ({
                "item_id" : item_id,
                "name" : menu[item_id]["name"],
                "qty" : qty,
                "price" : price
            })
            total += price
        else:
            print("Invalid item id!")

    orders.append
    ({
        "order_id" : order_id,
        "date" : date,
        "items" : order_items,
        "total" : total
    })            
    print("Order placed successfully!")

def delete_order():
    order_id = input("Enter order id to delete: ")

    for order in orders:
        if order["order_id"] == order_id:
            orders.remove(order)
            print("Order deleted successfully!")
            return

    print("Orders not found! \n")

#..............REPORT FUNCTONS...............

def daily_sales_report():
    date = input("Enter date (YYYY-MM-DD): ")
    total_sales = 0

    print("\n-----Daily sales report-----")
    for order in orders:
        if order["date"] == date:
            print(f"Order ID: {order['order_id']} | Amount: ${order['total']}")
            total_sales += order["total"]
    print(f"Total Sales on {date}: ${total_sales}\n")    

#.................EXTRA REPORT.....................

def top_selling_items():
    item_count = {}

    for order in orders:
        for item in order["items"]:
            if item["name"] in item_count:
                item_count[item["name"]] += item["qty"]    
            else:
                 item_count[item["name"]] = item["qty"] 
        print("\n...........TOP SELLIING ITEMS..............")
        sorted_items = sorted(item_count.items(), key=lambda x: x[1], reverse=True)

        for name, qty in sorted_items:
            print(f"{name} sold {qty} times")
        print()

#....................MAIN MENU..............................

def manager_panel():
    while True:
        print("1. Add/Update Menu")
        print("2. Place order")
        print("3. Delete Order")
        print("4. Daily Sales Report")
        print("5. Top selling itms Report")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_or_update_menu()
        elif choice == "2":
            place_order() 
        elif choice == "3":
            delete_order()
        elif choice == "4":
            daily_sales_report()
        elif choice == "5":
            top_selling_items()
        elif choice == "6":
            print("Exiting......")
            break
        else:
            print("Invalid choice! \n")    

#Run program
manager_panel()