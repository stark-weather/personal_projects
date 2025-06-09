import tkinter as tk
import tkinter as ttk 

"""Simple Version of Budget App"""
# Customized Exception
def UserInputError(Exception):
    pass

# Create window 
window = tk.Tk()

# Change title of the window
window.title("Fall Semester Budget App")

# Create widgets 
money_spent = ttk.Label(window, text = "How Much Did You Spend? ") 
money_input = ttk.Entry(window,  width = 30) # The number of characters a user can input
budget_text = ttk.Label(window, text = "Budget: ")
monthly_budget = ttk.Label(window, text = "250")
submit_button = ttk.Button(window, text = "Continue")

# Place widgets in window
money_spent.grid(row = 0, column = 0)
money_input.grid(row = 0, column = 1)
submit_button.grid(row = 0, column = 2)
budget_text.grid(row = 1, column = 0)
monthly_budget.grid(row = 1, column = 1)

def get_input() -> str:
    """Get User Input"""
    user_input = money_input.get()
    return user_input

def handle_input() -> list:
    """Handles User Input"""
    # Initialize list 
    amount_list = []
    # Call function to get user inputs 
    user_inputs = get_input()
    # Put user inputs into a list 
    input_list = user_inputs.split(',')
    # Convert str to float and add to empty list
    for dollars in input_list:
        dollars = float(dollars.strip())
        amount_list.append(dollars)
    return amount_list

def add_total() -> float:
    """Total Spendings"""
    # Call function to get list of amount 
    amount_list = handle_input()
    total_spendings = sum(amount_list)
    return total_spendings

def subtract_from_budget() -> float:
    """Leftover Budget"""
    budget = 250
    # Call function to get total spendings
    total_spendings = add_total()
    leftover = 250 - total_spendings
    return leftover

def display_leftover():
    """Display Message"""
    # Call function to get budget leftover 
    budget_leftover = subtract_from_budget()
    # Display leftover budget
    monthly_budget['text'] = str(budget_leftover)

# Functionality 
submit_button['command'] = display_leftover
# Run window
window.mainloop()