import tkinter as tk
from tkinter import messagebox

class MenuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Menu - GUI Version")
        self.root.geometry("350x400")
        self.root.configure(bg='lightblue')
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, 
                              text="Your Personal Menu", 
                              font=("Arial", 16, "bold"),
                              bg='lightblue', fg='darkblue')
        title_label.pack(pady=20)
        
        # Subtitle
        subtitle_label = tk.Label(self.root, 
                                 text="Please choose an Option:", 
                                 font=("Arial", 12),
                                 bg='lightblue')
        subtitle_label.pack(pady=10)
        
        # Buttons Frame
        buttons_frame = tk.Frame(self.root, bg='lightblue')
        buttons_frame.pack(pady=20)
        
        # Menu buttons (samma som din console version)
        btn1 = tk.Button(buttons_frame, text="Option 1", 
                        command=self.option1, width=15, height=2,
                        bg='lightgreen', font=("Arial", 10))
        btn1.pack(pady=5)
        
        btn2 = tk.Button(buttons_frame, text="Option 2", 
                        command=self.option2, width=15, height=2,
                        bg='lightcoral', font=("Arial", 10))
        btn2.pack(pady=5)
        
        btn3 = tk.Button(buttons_frame, text="Option 3", 
                        command=self.option3, width=15, height=2,
                        bg='lightyellow', font=("Arial", 10))
        btn3.pack(pady=5)
        
        btn4 = tk.Button(buttons_frame, text="Option 4", 
                        command=self.option4, width=15, height=2,
                        bg='lightpink', font=("Arial", 10))
        btn4.pack(pady=5)
        
        # Exit button
        exit_btn = tk.Button(buttons_frame, text="Exit", 
                           command=self.exit_app, width=15, height=2,
                           bg='red', fg='white', font=("Arial", 10, "bold"))
        exit_btn.pack(pady=15)
        
        # Output text area för att visa meddelanden
        self.output_text = tk.Text(self.root, height=6, width=40, 
                                  bg='white', font=("Arial", 10))
        self.output_text.pack(pady=10, padx=20)
        
        # Initial message
        self.log_message("Welcome! Choose an option above.")
        
    def log_message(self, message):
        """Add message to output text area"""
        self.output_text.insert(tk.END, f"{message}\n")
        self.output_text.see(tk.END)
        
    def option1(self):
        """Handle Option 1 - samma som din console kod"""
        self.log_message("| You chose Option 1 |")
        
    def option2(self):
        """Handle Option 2 - samma som din console kod"""
        self.log_message("You chose Option 2")
        
    def option3(self):
        """Handle Option 3 - samma som din console kod"""
        self.log_message("You chose Option 3")
        
    def option4(self):
        """Handle Option 4 - samma som din console kod"""
        self.log_message("you choose all options")
        
    def exit_app(self):
        """Exit the application - samma som din console kod"""
        self.log_message("Exiting...")
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.quit()

def main():
    root = tk.Tk()
    app = MenuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()