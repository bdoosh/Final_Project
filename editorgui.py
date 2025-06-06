import tkinter as tk 
from tkinter import ttk
import backenddata as bed


class MenuEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Editor")
        self.root.geometry("600x400")
        
        # configure grid layout
        # Silent_Creme is a uniform name for the grid columns I found about on Reddit!
        self.root.columnconfigure(0, weight=1, uniform="Silent_Creme")
        self.root.columnconfigure(1, weight=1, uniform="Silent_Creme")
        self.root.columnconfigure(2, weight=1, uniform="Silent_Creme")
        self.root.columnconfigure(3, weight=1, uniform="Silent_Creme")
        
        
        self.item_list = {}
        self.new_items = {}
                
        self.wbody = 50
        self.py = 5
        self.px = 5
        
        # App title
        self.menu_label = tk.Label(self.root, text="MENU EDITOR", anchor="center")
        self.menu_label.grid(row=0, column=1, columnspan=2, pady=10)
        
        # Line separator
        self.separator1 = ttk.Separator(self.root, orient="horizontal")
        self.separator1.grid(row=1, column=1, columnspan=2, sticky=tk.EW, padx=self.px)
        
        # Menu title
        self.title_label = tk.Label(self.root, text="Shop Name", width=self.wbody, anchor="center")
        self.title_label.grid(row=2, column=1, columnspan=2, padx=self.px, pady=self.py)
        
        # Menu description
        self.description_label = tk.Label(self.root, text="Shop Description", anchor="center")
        self.description_label.grid(row=3, column=1, columnspan=2, padx=self.px, pady=self.py)
        
        # Line separator
        self.separator2 = ttk.Separator(self.root, orient="horizontal")
        self.separator2.grid(row=4, column=1, columnspan=2, sticky=tk.EW, padx=self.px)
        
        # New items list
        self.item_label = tk.Label(self.root, text="ITEMS", anchor="center")
        self.item_label.grid(row=5, column=1, padx=self.px, pady=self.py)
        self.price_label = tk.Label(self.root, text="PRICE", anchor="center")
        self.price_label.grid(row=5, column=2, padx=self.px, pady=self.py)
        
        self.items_label = tk.Label(self.root, text="", anchor="center")
        self.items_label.grid(row=6, column=1, padx=self.px, pady=self.py)
        self.prices_label = tk.Label(self.root, text="", anchor="center")
        self.prices_label.grid(row=6, column=2, padx=self.px, pady=self.py)

        
        # Edit button
        self.edit_button = ttk.Button(self.root, text="Edit", command=self.editor)
        self.edit_button.grid(row=6, column=0, sticky=tk.NS, padx=self.px, pady=self.py)
        
        # Save & Exit button
        self.exit_button =ttk.Button(self.root, text="Save", command=self.save_exit)
        self.exit_button.grid(row=6, column=3, sticky=tk.NS, padx=self.px, pady=self.py)
        
    
    # Display editor
    def editor(self):
        # Removes widgets from home
        self.title_label.grid_forget()
        self.description_label.grid_forget()
        self.item_label.grid_forget()
        self.price_label.grid_forget()
        self.items_label.grid_forget()
        self.prices_label.grid_forget()
        self.separator1.grid_forget()
        self.separator2.grid_forget()
        self.edit_button.grid_forget()
        self.exit_button.grid_forget()
        
        # Edit shop name
        self.edit_title = tk.Label(self.root, text="Shop Name:")
        self.edit_title.grid(row=1, column=0, sticky=tk.E, padx=self.px, pady=self.py)
        self.entry_title = ttk.Entry(self.root, width=self.wbody)
        self.entry_title.insert(0, self.title_label.cget("text"))
        self.entry_title.grid(row=1, column=1, columnspan=2, pady=self.py)
        
        # Edit shop description
        self.edit_description = tk.Label(self.root, text="Description:")
        self.edit_description.grid(row=2, column=0, sticky=tk.E, padx=self.px, pady=self.py)
        self.entry_description = ttk.Entry(self.root, width=self.wbody)
        self.entry_description.insert(0, self.description_label.cget("text"))
        self.entry_description.grid(row=2, column=1, columnspan=2, pady=self.py)
        
        self.separator3 = ttk.Separator(self.root, orient="horizontal")
        self.separator3.grid(row=3, column=1, columnspan=2, sticky=tk.EW, pady=10)
        
        # Edit item name and price
        self.edit_item = tk.Label(self.root, text="Item Name:")
        self.edit_item.grid(row=4, column=0, sticky=tk.E, padx=self.px, pady=self.py)
        self.entry_item = ttk.Entry(self.root)
        self.entry_item.grid(row=4, column=1, sticky=tk.W, padx=self.px, pady=self.py)
        self.edit_price = tk.Label(self.root, text="Price:")
        self.edit_price.grid(row=5, column=0, sticky=tk.E, padx=self.px, pady=self.py)
        self.entry_price = ttk.Entry(self.root)
        self.entry_price.grid(row=5, column=1, sticky=tk.W, padx=self.px, pady=self.py)
        
        # Error message if wrong input
        self.error_label = tk.Label(self.root, text="", fg="red")
        self.error_label.grid(row=6, column=1, columnspan=2, pady=self.py)
        
        # Add item button
        self.add_button = ttk.Button(self.root, text="Add Item", command=self.addItem)
        self.add_button.grid(row=4, column=2, rowspan=2, sticky=tk.NS, padx=self.px, pady=self.py)
        
        # Update button
        self.update_button = ttk.Button(self.root, text="Update", command=self.update)
        self.update_button.grid(row=6, column=3, sticky=tk.NS, padx=self.px, pady=self.py)
    
    
    def addItem(self):
        item_name = self.entry_item.get()
        item_price = self.entry_price.get()
        
        if not item_name or not item_price: # Check if item name and price are valid
            self.error_label.config(text="Please fill in both fields")
        elif item_name.isdigit():
            self.error_label.config(text="Item name must contain only letters")
        elif not item_price.replace('.', '', 1).isdigit():
            self.error_label.config(text="Price must be a value (ex. 12.99, 7, 5.5)")
        
        else: # List new item list
            self.error_label.config(text="New item added successfully!", fg="green")
            
            item_price = f"${float(item_price):,.2f}"  # Format price to 2 decimal places
            
            self.item_list[item_name] = item_price # Add item to the item list dictionary
            
            self.new_items[item_name] = item_price # Add new items to display
            
            row_count = 0
            for name, price in self.new_items.items(): # Create new labels for item and price
                self.new_item_label = tk.Label(self.root, text=name, anchor="center")
                self.new_item_label.grid(row=7 + row_count, column=1, padx=self.px, pady=self.py)
                self.new_price_label = tk.Label(self.root, text=price, anchor="center")
                self.new_price_label.grid(row=7 + row_count, column=2, padx=self.px, pady=self.py)
                row_count += 1
        
            # Clear entry fields after adding item
            self.entry_item.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)
    
    
    def update(self):
        # Remove widgets from editor section
        self.edit_title.grid_forget()
        self.entry_title.grid_forget()
        self.edit_description.grid_forget()
        self.entry_description.grid_forget()
        self.edit_item.grid_forget()
        self.entry_item.grid_forget()
        self.edit_price.grid_forget()
        self.entry_price.grid_forget()
        self.error_label.grid_forget()
        self.new_item_label.grid_forget()
        self.new_price_label.grid_forget()
        self.add_button.grid_forget()
        self.update_button.grid_forget()
        self.separator3.grid_forget()
        
        self.new_items.clear()
        
        # Update new shop name
        new_title = self.entry_title.get()
        self.title_label.config(text=new_title)
        self.title_label.grid(row=2, column=1, columnspan=2, padx=self.px, pady=self.py)
        
        self.separator1.grid(row=1, column=1, columnspan=2, sticky=tk.EW, padx=self.px)
        
        # Update new shop description
        new_description = self.entry_description.get()
        self.description_label.config(text=new_description)
        self.description_label.grid(row=3, column=1, columnspan=2, padx=self.px, pady=self.py)
        
        self.separator2.grid(row=4, column=1, columnspan=2, sticky=tk.EW, padx=self.px)
        
        
        # Update item name and price
        self.item_label.grid(row=5, column=1, padx=self.px, pady=self.py)
        self.price_label.grid(row=5, column=2, padx=self.px, pady=self.py)
        
        row_count = 0
        for item, price in self.item_list.items():
            self.items_label = tk.Label(self.root, text=item, anchor="center")
            self.items_label.grid(row=6 + row_count, column=1, padx=self.px, pady=self.py)
            self.prices_label = tk.Label(self.root, text=price, anchor="center")
            self.prices_label.grid(row=6 + row_count, column=2, padx=self.px, pady=self.py)
            row_count += 1
        
        # Edit and exit buttons
        self.edit_button.grid(row=6, column=0, padx=self.px, pady=self.py)
        self.exit_button.grid(row=6, column=3, padx=self.px, pady=self.py)


    # Save info to json file and then exit app
    def save_exit(self):
        layout = {}
        layout.update({"title": self.getTitle()})
        layout.update({"description": self.getDescription()})
        bed.createJSON(layout)
        
        self.root.destroy()

        
    # Get title and description from labels
    def getTitle(self):
        return self.title_label.cget("text")
    
    
    def getDescription(self):
        return self.description_label.cget("text")
        

if __name__ == "__main__":
    root =tk.Tk()
    app = MenuEditor(root)
    root.mainloop()
    