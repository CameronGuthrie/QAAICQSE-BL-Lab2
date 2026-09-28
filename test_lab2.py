from Lab2 import PricingEngine

def test_calculate_item_price():
    engine = PricingEngine()
    item = {'price': 100}
    result = engine.calculate_item_price(item, 2, 'premium')
    assert result == 190  # 100 * 2 * 0.95
    
def test_apply_discounts():
    engine = PricingEngine()
    cart = [{'price': 100, 'quantity': 1}]
    result = engine.apply_discounts(cart, ['SAVE10'])
    assert result == 90

if __name__ == "__main__":
    test_calculate_item_price()
    print("test_calculate_item_price passed")
    
    test_apply_discounts()
    print("test_apply_discounts passed")