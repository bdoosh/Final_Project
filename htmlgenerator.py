# Generates html file
import backenddata as bed

class WebPage:
    def __init__(self, layout):
        self.layout = layout
    
        # Load the item list from layout
        self.item_list = self.layout.get("items", {})
        
        # Create or open index.html file
        self.page = open("index.html", "w")
        
    # Write html structure to the page
        self.page_title = f"<title>{self.layout.get('title')}</title>"
        
        self.shop_name = f"<h1 id='shopname'>{self.layout.get('title')}</h1>"
        
        self.description = f"<h4 id='shopdescription'>{self.layout.get('description')}</h4>"
        
        self.menu = "<h2 id='textmenu'>MENU</h2>"
        
        # Create menu list
        self.menu_list = "<div class='shopmenu'>\n        <div class='row'>\n"
        self.name_list = "            <div class='column'>\n"
        self.price_list = "            <div class='column'>\n"
        
        
        for name, price in self.item_list.items():
            self.name_list += f"                {name}<br>\n"
            self.price_list += f"                {price}<br>\n"
            
        self.name_list += "            </div>\n"
        self.price_list += "            </div>\n"
        
        self.menu_list += self.name_list + self.price_list + "        </div>\n        </div>\n"
        
        
        # Write html content to page
        self.page.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n" +
                        "    <meta charset='UTF-8'>\n" +
                        "    <link href='style.css' rel='stylesheet' type='text/css'>\n\n" +
                        f"    {self.page_title}\n" +
                        "</head>\n<body style='font-family: Arial'>\n" +
                        "    <div style='text-align: center; border-style: solid; border: width 3px; margin-top: 20px; padding: 20px;'>\n" +
                        f"        {self.shop_name}\n\n" +
                        f"        {self.description}\n\n" +
                        f"        {self.menu}\n\n" +
                        f"        {self.menu_list}\n" +
                        "    </div>\n</body>\n</html>")
    
        # Close page file
        self.page.close()
        
        self.getCSSFile()
     
     
    # Create css file   
    def getCSSFile(self):
        self.css = open("style.css", "w")
        
        self.shopname_css = "#shopname {\n    padding-top: 70px;\n    padding-bottom: 20px;\n}"
        
        self.descript_css = "#shopdescription {\n    padding-bottom: 40px;\n}"
        
        self.menu_css = "#textmenu {\n    padding-bottom: 10px;\n}"
        
        self.menulist_css = ".shopmenu {\n    padding-top: 50px;\n    padding-bottom: 50px;\n    line-height: 200%;\n    border-style: solid;\n    border-width: 1px;\n}"
        
        self.row_css = ".row {\n    display: flex;\n}"
        
        self.col_css = ".column {\n    flex: 50%;\n}"
        
        self.css.write(f"{self.shopname_css}\n\n{self.descript_css}\n\n{self.menu_css}\n\n" +
                       f"{self.menulist_css}\n\n{self.row_css}\n\n{self.col_css}\n\n" )
        
        self.css.close()
