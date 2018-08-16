from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'My item 1',
                'price': 15.09
            }
        ]
    }
]

# POST /stores {name} Creates a store with an empty list of items
@app.route('/stores', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(stores)

# GET /stores/<string:name> {A store}
@app.route('/stores/<string:name>')
def get_store(name):
   for store in stores:
       if store['name'] == name
           return jsonify(store)

# GET /stores {All stores}
@app.route('/stores')
def get_stores():
    return jsonify({'data': stores})

# POST /store/<string:name>/item {name, price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']

            }
            store['items'].append(new_item)
            return jsonify({'item': new_item})
    return jsonify({'message': 'store not found'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5000)
