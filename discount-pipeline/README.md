# Discount Pipeline Logic
This project demonstrates a modular "Writer/Caller" architecture for processing store discounts.

## ⚙️ Mechanical Trace
1. **Input:** `main.py` defines the item and price.
2. **Logic:** `engine.py` calculates the discount using a percentage formula.
3. **Pipeline:** The output of the calculation is passed directly into the receipt builder.
4. **Output:** A formatted string is printed to the terminal.

## 🛠️ Tech Stack
- Python 3.x
- Type Hinting (Mechanical Verification)
- Modular File Structure