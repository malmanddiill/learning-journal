import csv
from expense import Expense

class ExpenseTracker:
    """Simple CLI expense tracker."""
    
    def __init__(self):
        self.expenses = []
        self.filename = "expenses.csv"
    
    def add_expense(self, description, amount, category="Other"):
        """Add a new expense."""
        expense = Expense(description, amount, category)
        self.expenses.append(expense)
        print(f"✓ Added: {expense}")
    
    def list_expenses(self):
        """List all expenses."""
        if not self.expenses:
            print("No expenses yet.")
            return
        
        print("\n=== Your Expenses ===")
        total = 0
        for i, exp in enumerate(self.expenses, 1):
            print(f"{i}. {exp}")
            total += exp.amount
        print(f"\nTotal: ${total:.2f}")
    
    def save_to_csv(self):
        """Save expenses to CSV file."""
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["description", "amount", "category"])
            for exp in self.expenses:
                writer.writerow([exp.description, exp.amount, exp.category])
        print(f"✓ Saved {len(self.expenses)} expenses to {self.filename}")
    
    def load_from_csv(self):
        """Load expenses from CSV file."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                self.expenses = []
                for row in reader:
                    if row:  # Skip empty rows
                        self.add_expense(row[0], float(row[1]), row[2])
            print(f"✓ Loaded expenses from {self.filename}")
        except FileNotFoundError:
            print(f"No existing {self.filename} file. Starting fresh.")
    
    def get_float(self, prompt):
        """Safely get a float input."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a number (e.g., 12.50).")
    
    def run(self):
        """Main CLI loop."""
        self.load_from_csv()
        
        while True:
            print("\n=== Expense Tracker ===")
            print("1. Add expense")
            print("2. List expenses")
            print("3. Save to CSV")
            print("4. Exit")
            
            choice = input("\nChoose 1-4: ").strip()
            
            if choice == "1":
                desc = input("Description: ").strip()
                amount = self.get_float("Amount: $")
                category = input("Category (default: Other): ").strip() or "Other"
                self.add_expense(desc, amount, category)
            
            elif choice == "2":
                self.list_expenses()
            
            elif choice == "3":
                self.save_to_csv()
            
            elif choice == "4":
                if self.expenses:
                    save = input("Save before exiting? (y/n): ").strip().lower()
                    if save == "y":
                        self.save_to_csv()
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please choose 1-4.")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
