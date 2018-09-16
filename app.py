from flask import Flask, jsonify 
app=Flask(__name__)

#for the index page
@app.route('/')
def index():
    return jsonify({'about':'Welcome to Fast-Food-Fast API'})

#to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders':orders})

#to get a particular order using order_ID
@app.route('/orders/<int:order_ID>', methods=['GET'])
def get_one_order(order_ID):
    order = dict()
    for item in orders:
        if item['order_ID'] == order_ID:
            order = {
                'name': item['name'],
                'price': item['price']
            }
    return jsonify(order)

if __name__=='__main__':
    app.run(debug=True)