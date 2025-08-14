import tkinter as tk 
import tkinter as ttk
import tkinter.messagebox as msg
from datetime import datetime

class BudgetApp:
    """Budget App"""
    def __init__(self, window: any):
        # Instance variables
        self.window = window
        # Change title of window
        self.window.title("Fall Semester Budget App")
        # Update budget
        self.current_budget = self.update_budget()
        self.current_budget = self.cumulative_budget()
        # Call GUI
        self.create_gui()
        # Bind widget button to return key
        self.window.bind('<Return>', self.handle_return_key)

    def create_gui(self) -> None:
        """Create and Place Widgets"""
        self.money_spent = ttk.Label(self.window, text = "How Much Did You Spend? ")
        self.budget_text = ttk.Label(self.window, text = "Budget: ")
        self.monthly_budget = ttk.Label(self.window, text = str(self.current_budget))
        self.month_day = ttk.Label(self.window, text = str(self.current_month))
        self.money_input = ttk.Entry(self.window,  width = 30) # The number of characters a user can input
        self.submit_button = ttk.Button(self.window, text = "Continue", command = self.display_leftover)
        # Place widgets in window
        self.month_day.grid(row = 0, column = 2)
        self.money_spent.grid(row = 1, column = 0)
        self.money_input.grid(row = 1, column = 1)
        self.submit_button.grid(row = 1, column = 2)
        self.budget_text.grid(row = 2, column = 0)
        self.monthly_budget.grid(row = 2, column = 1)

    def get_input(self) -> str:
        """Get User Input"""
        user_input = self.money_input.get()
        return user_input
    
    def handle_input(self) -> list:
        """Handles User Input"""
        # Initialize list 
        amount_list = []
        # Call function to get user inputs 
        user_inputs = self.get_input()
        # Put user inputs into a list 
        input_list = user_inputs.split(',')
        # Convert str to float and add to empty list
        for dollars in input_list:
            dollars = float(dollars.strip())
            amount_list.append(dollars)
        return amount_list

    def add_money_spent(self) -> int:
        """Total Amount of Money Spent"""
        # Call function to get list of amount
        amount_list = self.handle_input()
        total_spendings = sum(amount_list)
        return total_spendings

    def subtract_from_budget(self) -> any:
        """Budget Leftover"""
        budget = 250.0
        # Call function to get total spendings
        total_spendings = self.add_money_spent()
        leftover = self.current_budget - total_spendings
        self.current_budget = leftover
        return leftover

    def clear(self) -> None:
        """Clear User Input"""
        # Deletes everything from the first character to the last
        self.money_input.delete(0, tk.END) 
    
    def handle_return_key(self, event) -> None:
        """Bind Widget Button To Return Key"""
        self.display_leftover()

    def display_message(self) -> None:
        """Display Warning Message"""
        if int(self.current_budget) < 100:
            msg.showinfo("WARNING")

    def save_to_file(self) -> None: 
        """Save Leftover Budget"""
        # Current year and month 
        self.current_month = datetime.now().strftime("%m-%d")
        with open("current_budget.txt", "w") as file:
            file.write(f" {self.current_budget},{self.current_month}")

    def update_budget(self) -> None:
        """Update Budget Label"""
        self.current_month = datetime.now().strftime("%m-%d")
        try:
            # Read the current budget in the file
            with open("current_budget.txt", "r") as file: 
                data = file.read().strip().split(',')
                self.save_budget = float(data[0])
                self.save_month = data[1]
                # Initialize current month
                self.current_month = datetime.now().strftime("%m-%d")
                # Check if it is a new month 
                if self.save_month == self.current_month:
                    return self.save_budget
                else:
                    return 250.0
        except (FileNotFoundError, ValueError):
            # Default value to display if there is nothing new to save
            return 250.0
        
    def cumulative_budget(self): 
        """Adding/Subtracting From Budget"""
        # Get today's date 
        today = datetime.now()
        # Initial budget for the month 
        new_budget = 250
        # Check if it is the first day of the month
        if today == 1:
            # Resets budget on the first of the month 
            if self.current_budget == 0:
                return new_budget
            # Add to next month budget (underspent)
            elif self.current_budget > 0:
                return new_budget + self.current_budget
            else:
                # Subtract from next month budget (overspent)
                return new_budget - abs(self.current_budget)
        else:
            # Current budget stays the same if it is not the first of the month 
            return self.current_budget

    def display_leftover(self) -> None:
        """Display New Budget"""
        # Call function to get budget leftover 
        budget_leftover = self.subtract_from_budget()
        # Display leftover budget
        self.monthly_budget['text'] = str(budget_leftover)
        self.budget_text['text'] = "New Budget: "
        # Save to file 
        self.save_to_file()
        # Clear input afterwards
        self.clear()
        # Display message if current budget is less than 100 dollars 
        self.display_message()

def main() -> None:
    """Main Function"""
    # Creates a new window
    window = tk.Tk()
    # Calls the class
    app = BudgetApp(window)
    # Runs the new window
    window.mainloop()

if __name__ == "__main__":
    main()
