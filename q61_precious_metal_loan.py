"""61. Calculate precious-metal loan interest with clear exceptions."""

RATES = {
    "gold": {18: 0.08, 22: 0.07, 24: 0.06},
    "silver": {925: 0.10, 950: 0.09, 999: 0.08},
    "platinum": {900: 0.07, 950: 0.06, 999: 0.05},
}


def calculate_interest(metal, purity, amount, tenure):
    try:
        key = metal.lower()
        if key not in RATES or purity not in RATES[key]:
            raise ValueError("Invalid metal or unsupported purity")
        return amount * RATES[key][purity] * tenure
    except TypeError:
        raise


try:
    print(calculate_interest("gold", 22, 500000, 2))
except (TypeError, ValueError) as error:
    print(error)
