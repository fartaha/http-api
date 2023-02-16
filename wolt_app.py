import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate_delivery_fee', methods=['POST'])
def calculate_delivery_fee():
    data = request.get_json()
    cart_value = data.get('cart_value')/100
    delivery_distance = data.get('delivery_distance')
    number_of_items = data.get('number_of_items')
    time = data.get('time')
    
    delivery_fee = 2
    surcharge = 0
    bulk_fee = 0
    
    # Check for small order surcharge
    if cart_value < 10:
        surcharge = 10 - cart_value
    
    # Calculate delivery fee based on distance
    if delivery_distance > 1000:
        extra_distance = delivery_distance - 1000
        extra_fee = extra_distance // 500
        if extra_distance % 500 != 0:
            extra_fee += 1
        delivery_fee += extra_fee
    
    # Calculate bulk fee
    if number_of_items >= 5:
        bulk_fee = (number_of_items - 4) * 0.5
        if number_of_items > 12:
            bulk_fee += 1.2
    total_fee = surcharge + delivery_fee + bulk_fee
    
    # Check for Friday rush
    friday_rush = "T17:00:00Z" <= time <= "T21:00:00Z"
    if friday_rush:
        total_fee *= 1.2
        if total_fee > 15:
            total_fee = 15

    # Check for free delivery
    if cart_value >= 100:
        response = jsonify({'delivery_fee': 0})
        return response

    if total_fee > 15:
        response = jsonify({'delivery_fee': 15*100})
        return response
    else:
        response = jsonify({'delivery_fee': int(total_fee*100)})
        return response

if  __name__ == '__main__':
	app.run(port=8000)