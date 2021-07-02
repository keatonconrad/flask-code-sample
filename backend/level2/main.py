from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    data = request.get_json()

    # Ensures article, cart, and delivery fee data are provided in the payload.
    # Also ensures at least one cart is present, per the specs in the README
    if (not all(key in data for key in ['articles', 'carts', 'delivery_fees']) or
            len(data['carts']) < 1):
        return {'message': 'Missing data'}, 400

    # Creates a mapping of the article ids to their respective prices for easier
    # access later
    article_id_to_price = {x['id']: x['price'] for x in data['articles']}
    output = {'carts': []}

    for cart in data['carts']:
        total = sum(article_id_to_price[item['article_id']] * item['quantity']
                    for item in cart['items'])

        for fee in data['delivery_fees']:
            if (fee['eligible_transaction_volume']['min_price'] <= total and
                    (fee['eligible_transaction_volume']['max_price'] is None or
                    total < fee['eligible_transaction_volume']['max_price'])):
                total += fee['price']
                break

        output['carts'].append({
            'id': cart['id'],
            'total': total
        })

    return output, 200


if __name__ == '__main__':
    app.run()
