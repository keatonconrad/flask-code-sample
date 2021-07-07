from flask import Flask, request
import math

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    data = request.get_json()

    # Ensures article, cart, delivery fee, and discount data are provided in the
    # payload. Also ensures at least one cart is present, per the specs in the
    # README
    required_data = ['articles', 'carts', 'delivery_fees', 'discounts']
    if not all(key in data for key in required_data) or len(data['carts']) < 1:
        return {'message': 'Missing data'}, 400

    output = {'carts': []}

    for cart in data['carts']:
        total = 0

        for item in cart['items']:
            article = next(a for a in data['articles'] if a['id'] == item['article_id'])
            price = article['price']

            discount_dict = next((d for d in data['discounts'] if d['article_id'] == item['article_id']), None)
            if discount_dict is not None:
                if discount_dict['type'] == 'amount':
                    price -= discount_dict['value']
                else:
                    price *= 1 - discount_dict['value'] / 100

            total += price * item['quantity']

        for fee in data['delivery_fees']:
            if (fee['eligible_transaction_volume']['min_price'] <= total and
                    (fee['eligible_transaction_volume']['max_price'] is None or
                    total < fee['eligible_transaction_volume']['max_price'])):
                total += fee['price']
                break

        output['carts'].append({
            'id': cart['id'],
            'total': math.floor(total)
        })

    return output, 200


if __name__ == '__main__':
    app.run()
