#********** Budget App **********
"""
This is a budget app used track spending on different categorie and visualizes the spending using a percentage chart.
"""
# Creating a Category class with:
# - deposit(), withdraw(), transfer(), get_balance(), and check_funds() methods.
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit(self, amount, description = ""):
        
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            
            self.ledger.append({'amount': amount * -1,  "description": description})
            return True
        else:
            return False


    def get_balance(self):
        total_amount = 0
        for item in self.ledger:
            total_amount += item['amount']
        return total_amount


    def transfer(self, amount, category, description = ""):
        if self.check_funds(amount):
            
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False


    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"

            items += f"{description:<23}{amount:>7}\n"
            total = f"Total: {self.get_balance():.2f}"

        return title + items + total



food = Category("Food")
food.deposit(500, "Initial Deposit")
food.withdraw(80, "veggies")
transport = Category("Transport")
food.transfer(100, transport)
clothing = Category("Clothing")
clothing.deposit(1200, "Initial Deposit")
entertainment = Category("Entertainment")
education = Category("Education")
print(food)
print(transport)

#  Creating the create_spend_chart(categories) function that:
# - Show percentage spent by category using withdrawals only.
# - Display percentages from 100 to 0 in steps of 10.
# - Use "o" for chart bars.
# - Add horizontal line and vertical category names.
def create_spend_chart(categories):
    

    total = 0
    percentages = []

    for category in categories:
        spent = 0

        for item in category.ledger:
            if item['amount'] < 0:
                spent += -item['amount']

        total += spent
        percentages.append(spent)

    percentages = [int((x / total) * 100) // 10 * 10 for x in percentages]

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{i:>3}|"

        for percent in percentages:
            if percent >= i:
                chart += " o "
            else:
                chart += "   "

        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(category.name) for category in categories)

    for i in range(max_len):
        chart += "     "

        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

        chart += "\n"

    return chart.rstrip("\n")