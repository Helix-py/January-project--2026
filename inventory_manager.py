import sqlite3

"""QUESTIONS I ASKED MYSELF BEFORE CODING AND ANSWERED AT THE END:

Q:how should the layout look like?  A: The layout follows the Previous LayoutWith Parent class add Item Child class remove Item child class Then see inventory child And then the main Loop.

Q:where does the data go in the db? A: In the sql db using update and insert into.

Q:how do i move data back and forth seemlessly? A: I had Python send commands and the database send back results.

Q:what errors might be a problem in use case of 1000+user recalls at once? A: sqlite3 will fail badly chose to not worry about this part.
"""

class inventory():

    def __init__(self, db_file):

        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.conn.execute("PRAGMA foreign_keys = 1;") #incase i want to add new tables (ex: shippers table)"


    def add_to_inventory(self):
        # 1 get inputs
        name = input("Enter item name: ").strip()
        category = input("Enter category name: ").strip()

         # 2 Validate inputs
        if not name or not category:
            print("Name and category cannot be empty!")
            return

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("quantity must be a positve")
                return
        except ValueError:
            print("must be a number")
            return

        # Step 3 & 4: Add or Update the item in the DATABASE
        cursor = self.conn.cursor()

        try:
            sql_insert = "INSERT INTO inventory (name, category, quantity) VALUES (?, ?, ?)"  # use placeholders (?) to prevent SQL injection, a major security risk.
            cursor.execute(sql_insert, (name.lower(), category.lower(), quantity))
            print(f"Added {quantity}  '{name}' in category '{category}'.")
        except sqlite3.IntegrityError:
            sql_update = """
                UPDATE inventory
                SET quantity = quantity + ?
                WHERE name = ? AND category = ?
            """
            cursor.execute(sql_update, (name.lower(), category.lower(), quantity))
            print(f"Updated '{name}', added {quantity}.")

        self.conn.commit()



    def remove_from_inventory(self):
        # 1 prompt for input
        name = input("Enter item name: ").strip()
        category = input("Enter category name: ").strip()


        # 2 Validate inputs
        if not name or not category:
            print("Name and category cannot be empty!")
            return

        try:
            quantity_to_remove = int(input("enter how much was taken from inventory: "))
            if quantity_to_remove <= 0:
                print("quantity must be a positve")
                return
        except ValueError:
            print("must be a number")
            return


        cursor = self.conn.cursor()

                        # Step 3: Check if the item exists and get its current quantity
        sql_select = "SELECT quantity FROM inventory WHERE name = ? AND category = ?"
        cursor.execute(sql_select, (name.lower(), category.lower()))
        result = cursor.fetchone()

        if result is None:
            print("Item not found in inventory.")
            return

        current_quantity = result[0]

        if quantity_to_remove > current_quantity:
            print(f"Error: Cannot remove {quantity_to_remove} {name}. Only {current_quantity} {name} in stock.")
        elif quantity_to_remove == current_quantity:
            sql_delete = "DELETE FROM inventory WHERE name = ? AND category = ?"
            cursor.execute(sql_delete, (name.lower(), category.lower()))
            print(f"Removed all {current_quantity} '{name}'. Item deleted from inventory.")
        else:
            update_sql = "UPDATE inventory SET quantity = quantity - ? WHERE name = ? AND category = ?"
            cursor.execute(update_sql, (quantity_to_remove, name.lower(), category.lower()))
            print(f"Removed {quantity_to_remove} '{name}'.")

        self.conn.commit()




    def see_inventory(self):

        cursor = self.conn.cursor()

        # Select all columns from the inventory table
        sql_select = "SELECT id, name, category, quantity FROM inventory ORDER BY category, name"
        cursor.execute(sql_select)

        all_items = cursor.fetchall()

        if not all_items:
            print("\n--- Inventory is empty ---")
            return

        print("\n--- Current Inventory ---")
        print(f"{'ID':<5}{'Name':<20}{'Category':<20}{'Quantity':<10}")
        print("-" * 55)
        for item in all_items:
            # item is a tuple, e.g., (1, 'apple', 'fruit', 10)
            print(f"{item[0]:<5}{item[1]:<20}{item[2]:<20}{item[3]:<10}")
        print("-" * 55)

    def __del__(self):
        """A destructor to ensure the connection is closed when the object is destroyed."""
        self.conn.close()

# --- Main Application Loop ---

db_file = 'inventory.db'
my_inventory = inventory(db_file)

while True:
    print("\n--- Inventory Menu ---")
    print("1. Add/Update item")
    print("2. See inventory")
    print("3. Remove item")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        my_inventory.add_to_inventory()
    elif choice == "2":
        my_inventory.see_inventory()
    elif choice == "3":
        my_inventory.remove_from_inventory()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")


