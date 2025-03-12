# Importing the tkinter module for GUI development
import tkinter as tk
from tkinter import messagebox  # Importing messagebox for displaying alerts and messages

# Function to calculate how long the budget will last
def calculate_budget():
    try:
        # Retrieve user input from the entry fields and convert to float
        total_budget = float(entry_total_budget.get())
        monthly_expenses = float(entry_total_expenses.get())

        # Calculate how many months the budget will last
        result_budget = total_budget / monthly_expenses

        # Display the result in a message box
        messagebox.showinfo("Final result", f"Your money will last for {result_budget:.2f} months.")

    except ValueError:
        # Show an error message if the user enters invalid input
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window for the application
root = tk.Tk()
root.title("Budget Calculator")  # Set the window title

# Create and place labels and input fields for budget and expenses
tk.Label(root, text="Enter your total budget (£):").grid(row=0, column=0, padx=10, pady=10)
entry_total_budget = tk.Entry(root)  # Entry field for total budget
entry_total_budget.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter your total monthly expenses (£):").grid(row=1, column=0, padx=10, pady=10)
entry_total_expenses = tk.Entry(root)  # Entry field for monthly expenses
entry_total_expenses.grid(row=1, column=1, padx=10, pady=10)

# Create and place the Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_budget)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop to run the application
root.mainloop()
