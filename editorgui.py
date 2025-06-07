import tkinter as tk 
from tkinter import ttk
import backenddata as bed
import htmlgenerator as htmlfile
import json


class MenuEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Editor")
        self.root.geometry("600x500")
        
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)
        self.root.columnconfigure(2, weight=1)
       
        self.item_list = {} # Dictionary to store items and their prices
        
        self.wbody = 30
        self.py = 5
        self.px = 5
        
        # App title
        self.menu_label = tk.Label(self.root, text="MENU EDITOR", anchor="center")
        self.menu_label.grid(row=0, column=1, pady=10, sticky=tk.EW)
        
        # Line separator
        self.separator1 = ttk.Separator(self.root, orient="horizontal")
        self.separator1.grid(row=1, column=1, pady=self.py, sticky=tk.EW)
        
        # Create left frame
        self.l_frame = ttk.Frame(self.root)
        self.l_frame.columnconfigure(0, weight=1)
        self.l_frame.grid(row=2, column=0, padx=self.px, sticky=tk.NS)
        
        # Create middle frame
        self.m_frame = ttk.Frame(self.root)
        self.m_frame.columnconfigure(0, weight=1)
        self.m_frame.columnconfigure(1, weight=1)
        self.m_frame.grid(row=2, column=1, sticky=tk.NSEW)
        
        # Create right frame
        self.r_frame = ttk.Frame(self.root)
        self.r_frame.columnconfigure(0, weight=1)
        self.r_frame.grid(row=2, column=2, padx=self.px, sticky=tk.NS)
        
        # Edit button
        self.edit_button = ttk.Button(self.l_frame, text="Edit", command=self.editor)
        self.edit_button.grid(row=0, column=0, padx=self.px, pady=self.py)
        
        # Load existing data from JSON file
        self.load_button = ttk.Button(self.l_frame, text="Load", command=self.load)
        self.load_button.grid(row=1, column=0, padx=self.px, pady=self.py)
        
        # Menu title
        self.title_label = tk.Label(self.m_frame, text="Shop Name", anchor="center")
        self.title_label.grid(row=1, column=0, columnspan=2, padx=self.px, pady=self.py)
        
        # Menu description
        self.description_label = tk.Label(self.m_frame, text="Shop Description", anchor="center")
        self.description_label.grid(row=2, column=0, columnspan=2, padx=self.px, pady=self.py)
        
        # Line separator
        self.separator2 = ttk.Separator(self.m_frame, orient="horizontal")
        self.separator2.grid(row=3, column=0, columnspan=2, pady=self.py, sticky=tk.EW)
        
        # Display items
        self.display_items = ttk.Treeview(self.m_frame, columns=("Item", "Price"), show="headings", height=15)
        self.display_items.column("Item", anchor='center', width=150)
        self.display_items.heading("Item", text="ITEM")
        self.display_items.column("Price", anchor='center', width=150)
        self.display_items.heading("Price", text="PRICE")
        self.display_items.grid(row=4, column=0,  columnspan=2, pady=self.py, sticky=tk.EW)
        
        self.confirm_label = tk.Label(self.m_frame, text="")
        
        # Save button
        self.save_button = ttk.Button(self.r_frame, text="Save", command=self.save)
        self.save_button.grid(row=0, column=0, padx=self.px, pady=self.py, sticky=tk.S)
   
    
    # Display editor
    def editor(self):
        # Removes widgets from home
        self.title_label.grid_forget()
        self.description_label.grid_forget()
        self.display_items.grid_forget()
        self.separator2.grid_forget()
        self.edit_button.grid_forget()
        self.save_button.grid_forget()
        self.load_button.grid_forget()
        self.confirm_label.config(text="")
        self.confirm_label.grid_forget()
        
        # Edit shop name
        self.edit_title = tk.Label(self.l_frame, text="Shop Name:")
        self.edit_title.grid(row=0, column=0, sticky=tk.E, padx=self.px, pady=self.py)
        self.entry_title = ttk.Entry(self.m_frame)
        self.entry_title.insert(0, self.title_label.cget("text"))
        self.entry_title.grid(row=0, column=0, columnspan=2, padx=self.px, pady=self.py, sticky=tk.EW)
           
        # Edit shop description  
        self.edit_description = tk.Label(self.l_frame, text="Description:")
        self.edit_description.grid(row=1, column=0, sticky=tk.E, padx=self.px, pady=self.py)
        self.entry_description = ttk.Entry(self.m_frame)
        self.entry_description.insert(0, self.description_label.cget("text"))
        self.entry_description.grid(row=1, column=0, columnspan=2, padx=self.px, pady=self.py, sticky=tk.EW)
        
        # Edit item name and price
        self.edit_item = tk.Label(self.l_frame, text="Item Name:")
        self.edit_item.grid(row=2, column=0, sticky=tk.E, padx=self.px, pady=self.py)
        self.entry_item = ttk.Entry(self.m_frame, width=self.wbody)
        self.entry_item.grid(row=2, column=0, sticky=tk.W, padx=self.px, pady=self.py)
        
        self.edit_price = tk.Label(self.l_frame, text="Price:")
        self.edit_price.grid(row=3, column=0, sticky=tk.E, padx=self.px, pady=self.py)
        self.entry_price = ttk.Entry(self.m_frame, width=self.wbody)
        self.entry_price.grid(row=3, column=0, sticky=tk.W, padx=self.px, pady=self.py)
        
        # Add item button
        self.add_button = ttk.Button(self.m_frame, text="Add Item", command=self.addItem)
        self.add_button.grid(row=2, column=1, rowspan=2, sticky=tk.NS, padx=self.px, pady=self.py)
            
        # Error message if wrong input
        self.error_label = tk.Label(self.m_frame, text="", fg="red")
        self.error_label.grid(row=4, column=0, columnspan=2, padx=self.px, pady=self.py)
        
        # Display new items added
        self.display_new_items = ttk.Treeview(self.m_frame, columns=("Item", "Price"), show="headings", height=9)
        self.display_new_items.column("Item", anchor='center', width=170)
        self.display_new_items.heading("Item", text="ITEM")
        self.display_new_items.column("Price", anchor='center', width=170)
        self.display_new_items.heading("Price", text="PRICE")
        self.display_new_items.grid(row=6, column=0, columnspan=2, pady=self.py)
        
        # Update button
        self.update_button = ttk.Button(self.r_frame, text="Update", command=self.update)
        self.update_button.grid(row=0, column=0, padx=self.px, pady=self.py)
        
    
    def addItem(self):
        item_name = self.entry_item.get().upper()
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

            self.display_new_items.insert("", "end", values=(item_name, item_price))
        
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
        
        self.edit_button.grid(row=0, column=0, padx=self.px, pady=self.py)
        self.load_button.grid(row=1, column=0, padx=self.px, pady=self.py)
        
        # Update new shop name
        new_title = self.entry_title.get()
        self.title_label.config(text=new_title)
        self.title_label.grid(row=1, column=0, columnspan=2, padx=self.px, pady=self.py)
        
        # Update new shop description
        new_description = self.entry_description.get()
        self.description_label.config(text=new_description)
        self.description_label.grid(row=2, column=0, columnspan=2, padx=self.px, pady=self.py)
        
        self.separator2.grid(row=3, column=0, columnspan=2, pady=self.py, sticky=tk.EW)
        
        for item in self.display_items.get_children(): # Clear previous items displayed
            self.display_items.delete(item)
            
        self.display_items.grid(row=4, column=0,  columnspan=2, pady=self.py, sticky=tk.EW)
        for item, price in self.item_list.items(): # Update item name and price
            self.display_items.insert("", "end", values=(item, price))
            
        self.save_button.grid(row=0, column=0, padx=self.px, pady=self.py, sticky=tk.S)


    # Save info to json file and then exit app
    def save(self):
        self.confirm_label.config(text="Menu saved successfully!", fg="green")
        self.confirm_label.grid(row=5, column=0, columnspan=2, padx=self.px, pady=self.py)
        
        layout = {}
        layout.update({"title": self.getTitle()}) # Add title to layout
        layout.update({"description": self.getDescription()}) # Add description to layout
        layout.update({"items": self.item_list})  # Add item list to layout
        bed.createJSON(layout) # Save layout to JSON file
        htmlfile.WebPage(layout)  # Generate HTML file with the updated layout


    def load(self):
        try:
            layout = bed.loadJSON()
        except FileNotFoundError: # If the file does not exist, return an empty dictionary
            self.confirm_label.config(text="No saved menu found.", fg="red")
            self.confirm_label.grid(row=5, column=0, columnspan=2, padx=self.px, pady=self.py)
            return {}
        except json.JSONDecodeError: # If the file is not a valid JSON, return an empty dictionary
            self.confirm_label.config(text="Error loading menu. Invalid JSON format.", fg="red")
            self.confirm_label.grid(row=5, column=0, columnspan=2, padx=self.px, pady=self.py)
            return {}
        
        self.title_label.config(text=layout.get("title"))
        self.description_label.config(text=layout.get("description"))
        
        for item in self.display_items.get_children(): # Clear previous items displayed
            self.display_items.delete(item)
            
        for item, price in layout.get("items", {}).items():
            self.display_items.insert("", "end", values=(item, price))
        
        self.item_list = layout.get("items", {}) # Restore item list from loaded data
        
        
    # Get title and description from labels
    def getTitle(self):
        return self.title_label.cget("text")
    
    
    def getDescription(self):
        return self.description_label.cget("text")
    
        
if __name__ == "__main__":
    root =tk.Tk()
    app = MenuEditor(root)
    root.mainloop()
    