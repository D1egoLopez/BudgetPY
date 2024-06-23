
from expense import Expense
import calendar
import datetime


def main():
    #starto
    print(f"Running Expense Tracker")
    expense_file_path = "expenses.csv"
    budget = 500

    

    # Get user to input their expense
    #expense = get_user_expense()

    # write it to a file
    #save_user_expense(expense, expense_file_path)

    # read said file and summerize expenses
    summerize_user_expense(expense_file_path, budget)


def get_user_expense():
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    #list of expense categories
    expense_categories = [
        "Rent", "Grocery", "Dining", "Shopping", "Utility",
        "Personal", "Phone", "Gym", "Travel", "Entertainment", "Cash"
    ]
    #Category selector, once seleccionado correctly it will crear la nueva expense
    while True:
        print("Select a category: ")

        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}, {category_name}")
        
        value_range = f"[1 - {len(expense_categories)}]"

        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("You were given a 1 to 11 range and you typed something else, are you ret.....?")


#Lo que dice el nombre de la funcion
def save_user_expense(expense: Expense, expense_file_path):
    print(f"saving expense : {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount} \n")



def summerize_user_expense(expense_file_path, budget):
    #List[Expense] es un indicator para el for loop so that it knows expenses 
    #es una lista de Expense
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(name=expense_name, category=expense_category, amount=float(expense_amount))
            expenses.append(line_expense)
    amount_by_category = {

    }
    #Con la key sacada el csv se saca la cantidad de dinero gastado
    #y se suma al gasto de esa expense segun su categoria(key)
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    
    #Un print mas bonico
    print("Expenses by category: ")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum([ex.amount for ex in expenses])
    print(f"You have spent ${total_spent:.2f} this month")

    money_left = budget - total_spent
    if money_left > 0:
        print(f"You have {money_left:.2f} left in your monthly budget")

    #que dia eh?

    #Giet current date
    now = datetime.datetime.now()
    #Number of days in month
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    #Remaining days in month
    remaining_days = days_in_month - now.day

    dayly_budget = money_left/remaining_days

    
    if  5 < dayly_budget < 10:
        print(f"You are getting closer to having to go on debt. Achica el gasto degenerado fiscal")
    elif 1 < dayly_budget <= 5:
        print("Para enfermo que nos quedamos sin plata")
    elif dayly_budget <= 1:
        print("Tas al horno hermano")
    
    if dayly_budget > 0:
        print(f"${dayly_budget:.2f} left to be spent in {remaining_days} days")
    elif dayly_budget < 0:
        print("''Restriccion presupuestaria a salido del grupo''")    

    


if __name__ == "__main__":
    main()