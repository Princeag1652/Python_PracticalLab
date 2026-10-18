store_1 = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15,
    "Monitor": 8
}

store_2 = {
    "Laptop": 5,
    "Mouse": 20,
    "Headphones": 12
}

store_3 = {
    "Keyboard": 10,
    "Monitor": 7,
    "Headphones": 8
}


# 1. Display inventory of a store
def display_inventory(store, store_name):
    print(f"\n{store_name} Inventory:")
    for product, quantity in store.items():
        print(f"{product}: {quantity}")


# 2. Check whether a product exists
def check_product(product, *stores):
    for index, store in enumerate(stores, start=1):
        if product in store:
            print(
                f"{product} exists in Store {index}: "
                f"{store[product]} units"
            )
        else:
            print(f"{product} not found in Store {index}")


# 3. Safely access stock using get()
def get_stock(product, store):
    return store.get(product, 0)


# 4. Merge inventories using dictionary comprehension
def merge_inventories(*stores):
    products = {product for store in stores for product in store}

    return {
        product: sum(store.get(product, 0) for store in stores)
        for product in products
    }


# 5. Update a dictionary with another inventory
def update_inventory(inventory, new_stock):
    inventory.update(new_stock)
    return inventory


# Main program
if __name__ == "__main__":
    display_inventory(store_1, "Store 1")
    display_inventory(store_2, "Store 2")
    display_inventory(store_3, "Store 3")

    print("\n--- Product Existence Check ---")
    check_product("Laptop", store_1, store_2, store_3)
    check_product("Printer", store_1, store_2, store_3)

    print("\n--- Safe Stock Access ---")
    print("Laptop in Store 1:", get_stock("Laptop", store_1))
    print("Printer in Store 1:", get_stock("Printer", store_1))

    print("\n--- Combined Inventory ---")
    combined = merge_inventories(store_1, store_2, store_3)

    for product, quantity in sorted(combined.items()):
        print(f"{product}: {quantity} units")

    print("\n--- Inventory Update ---")
    new_stock = {"Laptop": 3, "Printer": 6}
    update_inventory(combined, new_stock)

    print("After adding new stock records:")
    for product, quantity in sorted(combined.items()):
        print(f"{product}: {quantity} units")
