class PricingEngine:
    def __init__(self):
        self.tax_rates = {'US': 0.08, 'CA': 0.12}
        self.discount_codes = {'SAVE10': 0.10, 'WELCOME': 0.15}
        
    def calculate_item_price(self, item, quantity, customer_tier):
        base_price = item['price'] * quantity
        if customer_tier == 'premium':
            base_price *= 0.95
        return base_price
        
    def apply_discounts(self, cart, promotional_codes):
        total = sum(item['price'] * item['quantity'] for item in cart)
        for code in promotional_codes:
            if code in self.discount_codes:
                total *= (1 - self.discount_codes[code])
        return total