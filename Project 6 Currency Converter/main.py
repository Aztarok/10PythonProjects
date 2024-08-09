import json


def load_rates(json_file: str) -> dict[str, dict]:
    with open(json_file, "r") as file:
        return json.load(file)


def convert(amount: float, base: str, to: str, rates: dict[str, dict]) -> float:
    base = base.lower()
    to = to.lower()
    
    from_rates: dict | None = rates.get(base)
    to_rates: dict | None = rates.get(to)

    if to == "eur" and from_rates is not None:
        return amount / from_rates["rate"]

    if from_rates is not None and to_rates is not None:    
        if base == "eur":
            return amount * to_rates["rate"]
        else:
            return amount * (to_rates["rate"] / from_rates["rate"])
    else:
        print("This currency is not supported")
        print("Here is a list of all the currency you can exchange: ", list(rates.keys()))
        return 0

def main() -> None:
    rates: dict[str, dict] = load_rates("rates.json")
    result: float = convert(amount=10, base="usd", to="eur", rates=rates)
    print(result)

if __name__ == "__main__":
    main()