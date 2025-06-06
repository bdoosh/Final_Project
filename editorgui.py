import tkinter as tk 
from tkinter import ttk
import backenddata as bed


class MenuEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Editor")
        self.root.geometry("600x500")
        
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)
        self.root.columnconfigure(2, weight=1)
        
    
        # configure grid layout
        # Silent_Creme is a uniform name for the grid columns I found about on Reddit!
    
        
        self.item_list = {} # Dictionary to store items and their prices
        self.new_items = {} # Dictionary to store new items added in the editor
        
        self.wbody = 50
        self.wlabel = 30
        self.py = 5
        self.px = 5
        
        self.l_frame = self.leftFrame(self.root)
        self.l_frame.grid(row=0, column=0)
        
        self.r_frame = self.rightFrame(self.root)
        self.r_frame.grid(row=0, column=2)
        
        self.mid_frame = self.midFrame(self.root)
        self.mid_frame.grid(row=0, column=1, sticky=tk.NSEW)
        
        
    def leftFrame(self, container):
        frame = ttk.Frame(container)
        frame.columnconfigure(0, weight=1)
        
        # Edit button
        self.edit_button = ttk.Button(frame, text="Edit", command=self.editor)
        self.edit_button.grid(row=0, column=0, padx=self.px, pady=self.py, sticky=tk.S)
        
        return frame
    
       
    def rightFrame(self, container):
        frame = ttk.Frame(container)
        frame.columnconfigure(0, weight=1)
        
        # Save button
        self.save_button = ttk.Button(frame, text="Save", command=self.save_exit)
        self.save_button.grid(row=0, column=0, padx=self.px, pady=self.py, sticky=tk.S)
        
        return frame 
    
    
    def midFrame(self, container):
        frame = ttk.Frame(container)
        frame.columnconfigure(0, weight=3)
        
        # App title
        self.menu_label = tk.Label(frame, text="MENU EDITOR", anchor="center")
        self.menu_label.grid(row=0, column=0, pady=10)
        
        # Line separator
        self.separator1 = ttk.Separator(frame, orient="horizontal")
        self.separator1.grid(row=1, column=0, sticky=tk.EW, padx=self.px)
        
        # Menu title
        self.title_label = tk.Label(frame, text="Shop Name", anchor="center")
        self.title_label.grid(row=2, column=0, padx=self.px, pady=self.py)
        
        # Menu description
        self.description_label = tk.Label(frame, text="Shop Description", anchor="center")
        self.description_label.grid(row=3, column=0, padx=self.px, pady=self.py)
        
        # Line separator
        self.separator2 = ttk.Separator(frame, orient="horizontal")
        self.separator2.grid(row=4, column=0, sticky=tk.EW, padx=self.px)
        
        self.display_items = ttk.Treeview(frame, columns=("Item", "Price"), show="headings", height=15)
        self.display_items.column("Item", anchor='center', width=100)
        self.display_items.heading("Item", text="ITEM")
        self.display_items.column("Price", anchor='center', width=100)
        self.display_items.heading("Price", text="PRICE")
        self.display_items.grid(row=5, column=0, padx=self.px, pady=self.py, sticky=tk.EW)
        
        return frame
        
        
    # Display editor
    def editor(self):
        # Removes widgets from home
        self.title_label.grid_forget()
        self.description_label.grid_forget()
        self.display_items.grid_forget()
        self.separator1.grid_forget()
        self.separator2.grid_forget()
        self.edit_button.grid_forget()
        self.save_button.grid_forget()
        
        # Edit shop name
        self.edit_title = tk.Label(self.root, text="Shop Name:")
        self.edit_title.grid(row=1, column=0, sticky=tk.E, padx=self.px, pady=self.py)
        self.entry_title = ttk.Entry(self.root, width=self.wbody)
        self.entry_title.insert(0, self.title_label.cget("text"))
        self.entry_title.grid(row=1, column=1, columnspan=2, padx=self.px, pady=self.py)
        
        # Edit shop description
        self.edit_description = tk.Label(self.root, text="Description:")
        self.edit_description.grid(row=2, column=0, sticky=tk.E, padx=self.px, pady=self.py)
        self.entry_description = ttk.Entry(self.root, width=self.wbody)
        self.entry_description.insert(0, self.description_label.cget("text"))
        self.entry_description.grid(row=2, column=1, columnspan=2, padx=self.px, pady=self.py)
        
        self.separator3 = ttk.Separator(self.root, orient="horizontal")
        self.separator3.grid(row=3, column=1, columnspan=2, sticky=tk.EW, pady=10, padx=self.px)
        
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
        self.error_label.grid(row=6, column=1, columnspan=2, padx=self.px, pady=self.py)
        
        # Add item button
        self.add_button = ttk.Button(self.root, text="Add Item", command=self.addItem)
        self.add_button.grid(row=4, column=2, rowspan=2, sticky=tk.NS, padx=self.px, pady=self.py)
        
        self.display_new_items = ttk.Treeview(self.root, columns=("Item", "Price"), show="headings", height=9)
        self.display_new_items.column("Item", anchor='center', width=100)
        self.display_new_items.heading("Item", text="ITEM")
        self.display_new_items.column("Price", anchor='center', width=100)
        self.display_new_items.heading("Price", text="PRICE")
        self.display_new_items.grid(row=7, column=1, columnspan=2, padx=self.px, pady=self.py, sticky=tk.EW)    
        
        # Update button
        self.update_button = ttk.Button(self.root, text="Update", command=self.update)
        self.update_button.grid(row=8, column=3, sticky=tk.W, padx=self.px, pady=self.py)
    
    
    def addItem(self):
        item_name = self.entry_item.get()
        item_price = self.entry_price.get()
        
        if not item_name or not item_price: # Check if item name and price are valid
            self.error_label.config(text="Please fill in both fields")
            
        elif not all(c.isalpha() or c.isspace() for c in item_name): # Check if item name contains only letters
            self.error_label.config(text="Item name must contain only letters")
            
        elif not item_price.replace('.', '', 1).isdigit(): # Check if item price is a valid number
            self.error_label.config(text="Price must be a value (ex. 12.99, 7, 5.5)")
        
        else: # List new item list
            self.error_label.config(text="New item added successfully!", fg="green")
            
            item_price = f"${float(item_price):,.2f}"  # Format price to 2 decimal places
            
            self.item_list[item_name] = item_price # Add item to the item list dictionary
            
            self.new_items[item_name] = item_price # Add new items to display
  
            for name, price in self.new_items.items(): # Insert and display new added items
                self.display_new_items.insert("", "end", values=(name, price))
        
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
        self.display_new_items.grid_forget()
        self.add_button.grid_forget()
        self.update_button.grid_forget()
        self.separator3.grid_forget()
        
        self.new_items.clear() # Clear new items dictionary
        
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
        
        self.display_items.grid(row=5, column=1, columnspan=2, padx=self.px, pady=self.py, sticky=tk.EW)
        for item, price in self.item_list.items(): # Update item name and price
            self.display_items.insert("", "end", values=(item, price))
        
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
    