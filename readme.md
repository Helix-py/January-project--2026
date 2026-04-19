## **Inventory Management System**

## **Overview**

This repository contains a professional **Inventory Management System** developed in **January 2026**. The project was created as a practical application for mastering advanced Pythonic concepts, specifically focusing on **File Handling**, **Generators**, and **Decorators** to create clean, scalable, and memory-efficient code.

The system uses an Object-Oriented Programming (OOP) approach, featuring a base `item` class and a derived `Inventory` class to manage stock with data validation and streamlined processing.

---

## **Core Features**

* **OOP Architecture**: Utilizes inheritance to maintain a clear structure between item definitions and inventory logic.  
* **Memory Efficiency**: Implements a `generator` (`inventory_generator`) to yield items one by one, ensuring the system remains performant even as the inventory grows.  
* **Input Validation**: Robust error handling for user inputs to prevent crashes from invalid data types or negative numbers.  
* **Smart Updates**: Automatically detects if an item already exists in a category and updates the quantity rather than creating duplicate entries.

---

## **Running on PythonAnywhere**

Since this code was developed and optimized for **PythonAnywhere**, follow these steps to run it in that environment:

1. **Log in** to your PythonAnywhere account.  
2. **Upload the file**:  
   * Go to the **Files** tab.  
   * Upload your script (e.g., `inventory.py`) or create a new file and paste the code.  
3. **Open a Console**:  
   * Click on the file to open the editor.  
   * Click the **"Run this file"** button at the top right, OR:  
   * Go to the **Consoles** tab and start a new **Bash** console.  
4. **Execute the script**:  
   In the Bash console, type:

python3 inventory.py

5. 

---

## **How to Use**

Once the script is running, you will be presented with a text-based menu:

1. **Add Item**: Enter the name, category, and quantity. The system will create a new record or update an existing one.  
2. **See Inventory**: Displays all current items. This uses a **generator** to iterate through the data efficiently.  
3. **Remove Item**: Deducts a specific quantity from an item. If the quantity reaches zero, the item is automatically removed from the list.  
4. **Exit**: Safely closes the application.

---

## **Technical Note**

This project was a milestone in learning **File Handling** and **Decorators**. While the current version runs in-memory, the structure is designed to be easily extended with decorators for logging and file-handling methods for persistent data storage.

---

