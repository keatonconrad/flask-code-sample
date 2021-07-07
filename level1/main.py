from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    data = request.get_json()

    # Ensures article and cart data are provided in the payload.
    # Also ensures at least one cart is present, per the specs in the README
    if (not all(key in data for key in ['articles', 'carts']) or
            len(data['carts']) < 1):
        return {'message': 'Missing data'}, 400

    # Creates a mapping of the article ids to their respective prices for easier
    # access later
    article_id_to_price = {x['id']: x['price'] for x in data['articles']}
    output = {'carts': []}

    for cart in data['carts']:
        total = sum(article_id_to_price[item['article_id']] * item['quantity']
                    for item in cart['items'])
        output['carts'].append({
            'id': cart['id'],
            'total': total
        })

    return output, 200


if __name__ == '__main__':
    app.run()
