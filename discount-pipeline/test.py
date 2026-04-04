from engine import get_discount_price

def test_discount_logic():
    """
    Automated test to verify the discount math.
    """
    print("🧪 Running Test: 20% off $100...")
    
    # Expected result: 100 - 20 = 80
    result = get_discount_price(100.0, 20.0)
    
    if result == 80.0:
        print("✅ SUCCESS: Result is $80.00")
    else:
        print(f"❌ FAILED: Expected 80.0 but got {result}")

if __name__ == "__main__":
    test_discount_logic()