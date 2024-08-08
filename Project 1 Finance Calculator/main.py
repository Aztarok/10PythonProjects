def calculator_finances(monthly_income: float, tax_rate: float, currency: str, food_expenses: float, rent_expenses: float, gym_membership: float) -> None:
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    monthly_expenses: float = food_expenses + rent_expenses + gym_membership
    monthy_after_expenses: float = monthly_income - monthly_expenses
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax
    yearly_expenses: float = monthly_expenses * 12
    yearly_after_expenses: float = yearly_net_income - yearly_expenses
    
    print("--------------------------------------------")
    print(f"Monthly Income: {currency}{monthly_income:,.2f}")
    print(f"Tax Rate: {tax_rate:,.0f}%")
    print(f"Montly Tax: {currency}{monthly_tax:,.2f}")
    print(f"Monthly Net Income: {currency}{monthly_net_income:,.2f}")
    print(f"Yearly Salary: {currency}{yearly_salary:,.2f}")
    print(f"Yearly Tax: {currency}{yearly_tax:,.2f}")
    print(f"Yearly Net Income: {currency}{yearly_net_income:,.2f}")
    print(f"Monthly Net Income After Expenses: {currency}{monthy_after_expenses:,.2f}")
    print(f"Yearly Net Income After Expenses: {currency}{yearly_after_expenses:,.2f}")
    print("--------------------------------------------")
    

def main() -> None:
    while True:
        try:
            monthy_input: float = float(input("Enter your monthly salary: "))
            tax_rate: float = float(input("Enter your tax rate (%): "))
            food_expenses: float = float(input("Enter your monthly food expenses: "))
            rent_expenses: float = float(input("Enter your monthly rent expenses: "))
            gym_membership: float = float(input("Enter your monthly gym expenses: "))
            if type(monthy_input) == float and type(tax_rate) == float and type(food_expenses) == float and type(rent_expenses) == float and type(gym_membership) == float:
                break
        except ValueError:
            print("Please enter a valid number")
    calculator_finances(monthy_input, tax_rate, "$", food_expenses, rent_expenses, gym_membership)

if __name__ == "__main__":
    main()
