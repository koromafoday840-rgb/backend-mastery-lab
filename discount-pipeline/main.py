# Copy and paste this into main.py

# Step 1: Import your tools from the engine
from engine import get_discount_price, build_receipt

# Step 2: Set the raw data (The Input)
item_name = "Professional Clippers"
retail_price = 50.0
discount_rate = 15.0  # 15% off

# Step 3: Run the Pipeline (The Process)
# First, get the math done
final_total = get_discount_price(retail_price, discount_rate)

# Second, turn that math into a message
receipt_message = build_receipt(item_name, final_total)

# Step 4: Display the result (The Output)
print(receipt_message)