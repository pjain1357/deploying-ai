
tools = [
    {
        "type": "function",
        "name": "convert_currency",
        "description": "Convert an amount of money from one currency to another.",
        "parameters": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "number",
                    "description": "The numerical amount of money to convert."
                },
                "from_currency": {
                    "type": "string",
                    "description": "The ISO currency code for the source (e.g., USD, EUR)."
                },
                "to_currency": {
                    "type": "string",
                    "description": "The ISO currency code for the target (e.g., JPY, GBP)."
                }
            },
            "required": ["amount", "from_currency", "to_currency"],
            "additionalProperties": False,
        },
        "strict": True,
    }
]

def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    # Hardcoded exchange rates for simplicity
    """Convert the amount using the hardcoded exchange rates and return a formatted string with the result."""
    rates = {
        "USD_TO_EUR": 0.92,
        "USD_TO_GBP": 0.79,
        "EUR_TO_USD": 1.09
    }
    
    pair = f"{from_currency.upper()}_TO_{to_currency.upper()}"
    
    if pair in rates:
        converted = amount * rates[pair]
        return f"{amount} {from_currency} is equal to {converted:.2f} {to_currency}."
    else:
        return f"Error: Exchange rate for {pair} is not available."