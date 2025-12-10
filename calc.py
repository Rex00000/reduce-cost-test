def apply_discount(price, discount_rate):
    if not 0 <= discount_rate <= 1:
        raise ValueError("discount_rate must be between 0 and 1")

    return price * (1 - discount_rate)

def calculate_tax(price, tax_rate):
    return price * (1 + tax_rate)
