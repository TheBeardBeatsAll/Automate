# Display inventory on separate lines
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))

# Add items to inventory
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.setdefault(item, 0) + 1
    return inventory

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)