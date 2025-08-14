import tkinter as tk
import tkinter as ttk

"""Participation"""
def grade_display(frame, category, weight, row) -> dict:
    """Display for Each Grade Breakdown"""
    # Label for each category 
    label = ttk.Label(frame, text = f"{category}")
    label.grid(row = row, column = 0, sticky = "w")

    # Dropdwon for number of items
    num_items = tk.StringVar()
    # Default value
    num_items.set("1")
    # Create dropdown menu for the amount of items
    num_items_dropdown = ttk.OptionMenu(frame, num_items, *[str(item) for item in range(1, 11)])
    num_items_dropdown.grid(row = row, column = 1)

    # Dropdown for weight of each grade 
    weight_var = tk.StringVar()
    weight_var.set(str(weight))
    weight_dropdown = ttk.OptionMenu(frame, weight_var, *[str(diff_weight) for diff_weight in range(0, 51)])
    weight_dropdown.grid(row = row, column = 2)

    # Grade entries
    grade_entry = ttk.Entry(frame, width = 30)
    grade_entry.grid(row = row, column = 3)

    # Return variables 
    return {
        "Category": category,
        "Number of Items": num_items,
        "Weight": weight_var,
        "Grades": grade_entry
    }
