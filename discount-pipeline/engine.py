# Copy and paste this into engine.py

def get_discount_price(price: float, discount_percent: float) -> float:
    """
    Calculates the final price after a percentage reduction.
    Formula: Price * (1 - Rate/100)
    """
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return round(final_price, 2)

def build_receipt(product: str, final_price: float) -> str:
    """
    Formats the final result for a human to read.
    """
    return f"--- RECEIPT ---\nProduct: {product}\nTotal Due: ${final_price}\n---------------"