def calculate_split(total_amount: float, number_of_people: int, currency: str, uneven_list: list = []) -> None:
    if number_of_people < 1:
        raise ValueError("Number of people must be greater than one.")
    
    share_per_person: float = total_amount / number_of_people
    
    print(f"Total expenses: {currency}{total_amount:,.2f}")
    print(f"Number of people: {number_of_people}")
    if len(uneven_list) > 1:
        for i in range(len(uneven_list)):
            print(f"Person {i+1} should pay: {currency}{uneven_list[i]:,.2f}")
    else:
        print(f"Each person should pay: {currency}{share_per_person:,.2f}")

def main() -> None:
    while True:
        try:
            uneven_list = []
            total_amount: float = float(input("Enter total amount: "))
            number_of_people: int = int(input("Enter the number of people sharing the expense: "))
            uneven_splits: bool = input("Uneven splits? (y/n): ").lower() == "y"
            price_check: float = 0
            if uneven_splits:
                while True:
                    try:
                        for i in range(number_of_people):
                            share_amount: float = float(input("Enter share percentage for each person: "))
                            uneven_list.append(share_amount)
                            price_check += share_amount
                        if price_check < 100:
                            uneven_list.clear()
                            raise ValueError
                        else:
                            calculate_split(total_amount, number_of_people, "$", uneven_list)
                            break
                    except ValueError:
                        print("Error: The sum of the share percentages must equal 100%. Try Again.")
            else:
                calculate_split(total_amount, number_of_people, "$")
            if type(total_amount) == float:
                break
        except ValueError as e:
            print(f"Error: {e}")        

if __name__ == "__main__":
    main()