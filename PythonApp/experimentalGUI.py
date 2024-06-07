import tkinter as tk
from tkinter import messagebox
import pythonApp

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        
        # Manubar
        self.menubar = tk.Menu(self.root)
        
        # File Menu
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without Question", command=exit)
        
        # Add file menu to menubar
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        
        # Action Menu
        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)
        
        # Add action menu to menubar
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")
        
        # Configure root menu
        self.root.config(menu=self.menubar)
        
        # Name of interface
        self.root.geometry("500x500")
        self.root.title("Main Menu")
        
        # Creating the GUI label
        self.label = tk.Label(self.root, text="People and Cities of The World", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)
        
        # Displaying menu
        self.label_menu = tk.Label(self.root, text=self.get_menu_text(), font=('Arial', 12), justify="left")
        self.label_menu.pack(padx=20, pady=20)
        
        # Text box for user's choice
        self.user_input = tk.Entry(self.root)
        self.user_input.pack()
        
        # Button for confirming choice
        self.confirm_button = tk.Button(self.root, text="Confirm", font=('Arial', 10), command=self.handle_choice)
        self.confirm_button.pack(padx=20 , pady=5)
        
        # Closing message
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.display_menu()  # Call display_menu to initially show the menu
        
        self.root.mainloop()
    
    def get_menu_text(self):
        menu_text = "="*33 + "\n"
        menu_text += "{:^33}".format("MENU") + "\n"
        menu_text += "="*33 + "\n"
        menu_text += "1 - View Cities by County\n"
        menu_text += "2 - Update City Population\n"
        menu_text += "3 - Add New Person\n"
        menu_text += "4 - Delete Person\n"
        menu_text += "5 - View Countries by population\n"
        menu_text += "6 - Show Twinned Cities\n"
        menu_text += "7 - Twin with Dublin\n"
        menu_text += "x - Exit application\n"
        return menu_text
    
    def show_message(self):
        messagebox.showinfo(title="Message", message=self.user_input.get())
            
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            print("Goodbye from Planet Earth!")
            self.root.destroy()
            
    def handle_choice(self):
        choice = self.user_input.get().strip()  # Remove leading/trailing whitespace
        if choice == "1":
            self.user_input.delete(0, tk.END)  # Clear the entry widget
            pythonApp.cities_by_country()
            self.root.after(1000, self.display_menu)  # Wait for 1 second and then show the menu again
        elif choice == "2":
            self.user_input.delete(0, tk.END)
            pythonApp.city_population()
            self.root.after(1000, self.display_menu)
        elif choice == "3":
            self.user_input.delete(0, tk.END)
            pythonApp.add_person()
            self.root.after(1000, self.display_menu)
        elif choice == "4":
            self.user_input.delete(0, tk.END)
            pythonApp.delete_person()
            self.root.after(1000, self.display_menu)
        elif choice == "5":
            self.user_input.delete(0, tk.END)
            pythonApp.countries_by_population()
            self.root.after(1000, self.display_menu)
        elif choice == "6":
            self.user_input.delete(0, tk.END)
            pythonApp.show_twin_cities()
            self.root.after(1000, self.display_menu)
        elif choice == "7":
            self.user_input.delete(0, tk.END)
            pythonApp.twin_with_Dublin()
            self.root.after(1000, self.display_menu)
        elif choice == "x":
            self.on_closing()
        else:
            print("Invalid choice. Please try again.")
            
    def display_menu(self):
        self.label_menu.config(text=self.get_menu_text())

MyGUI()

# References: NeuralNine - Let's Develop Brains : https://wwww.neuralnine.com/


