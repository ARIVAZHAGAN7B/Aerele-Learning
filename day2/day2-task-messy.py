def process_order(order):
    total = 0
    for item in order['items']:
        price = item['price']
        qty = item['qty']
        if item.get('discount'):
            if item['discount_type'] == 'percent':
                price = price - (price * item['discount'] / 100)
            elif item['discount_type'] == 'flat':
                price = price - item['discount']
            if price < 0:
                price = 0
        total += price * qty
    if order.get('coupon'):
        if order['coupon'] == 'SAVE10':
            total = total * 0.9
        elif order['coupon'] == 'SAVE20':
            total = total * 0.8
    tax = 0
    if order['country'] == 'IN':
        tax = total * 0.18
    elif order['country'] == 'US':
        tax = total * 0.07
    else:
        tax = total * 0.10
    total = total + tax
    if order['customer']['type'] == 'premium':
        if total > 1000:
            total = total - 50
    shipping = 0
    if total < 500:
        shipping = 40
    total = total + shipping
    receipt = f"Order for {order['customer']['name']}: total = {total}"
    print(receipt)
    return total

sample_order = {
    'items': [
        {'price': 500, 'qty': 2, 'discount': 10, 'discount_type': 'percent'},
        {'price': 300, 'qty': 1, 'discount': 50, 'discount_type': 'flat'},
        {'price': 150, 'qty': 3},
    ],
    'country': 'IN',
    'customer': {'name': 'Arivazhagan', 'type': 'premium'},
    'coupon': 'SAVE10',
}

final_total = process_order(sample_order)
print("Returned value:", final_total)