class Expense:
    """Simple Expense class to track spending."""
    
    def __init__(self, description, amount, category="Other"):
        self.description = description
        self.amount = float(amount)
        self.category = category
    
    def __str__(self):
        return f"{self.description}: ${self.amount:.2f} ({self.category})"
    
    def __repr__(self):
        return f"Expense('{self.description}', {self.amount}, '{self.category}')"
    
    def is_expensive(self, threshold=100):
        """Check if expense exceeds threshold."""
        return self.amount > threshold
    
    def get_summary(self):
        """Return a formatted summary."""
        return f"{self.category} - {self.description}: ${self.amount:.2f}"


# Test the class
if __name__ == "__main__":
    # Create some expenses
    e1 = Expense("Coffee", 5.50, "Food")
    e2 = Expense("Laptop", 1200, "Electronics")
    e3 = Expense("Bus ticket", 2.50, "Transport")
    
    # Print them
    print(e1)
    print(e2)
    print(e3)
    print()
    
    # Test methods
    print(f"Is laptop expensive? {e2.is_expensive()}")
    print(f"Is coffee expensive? {e1.is_expensive()}")
    print()
    
    # Get summaries
    print("Summaries:")
    print(e1.get_summary())
    print(e2.get_summary())
    print(e3.get_summary())
