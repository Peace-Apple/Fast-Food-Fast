from flask import Flask, jsonify 
app=Flask(__name__)

#for the index page
@app.route('/')
def index():
    return jsonify({'about':'Welcome to Fast-Food-Fast API'})

#to get all orders
@app.route('/orders/', methods=['GET'])
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
                'email': item['email'],
                'contact': item['contact'],
                'location': item['location'],
                'food_item': item['food_item'],
                'no_of_items': item['no_of_items'],
                'price': item['price'],
                'delivery_time': item['delivery_time'],
                'order_ID': item['order_ID'],
                'payment': item['payment']
                
            }
    return jsonify(order)
#the orders defined
orders = [
    {
        'name': 'Omech',
        'email': 'omechemma@gmail.com',
        'contact': '0706346702',
        'location': 'Lubowa',
        'food_item': 'Chicken and Chips',
        'no_of_items':'2',
        'price': 15000,
        'delivery_time':'11.30pm',
        'order_ID': 1010,
        'payment': 'cash on delivery',
    },
    {
        'name': 'Apple',
        'email': 'astonreba@gmail.com',
        'contact': '0771904376',
        'location': 'Mbuya',
        'food_item': 'Chicken Luwombo',
        'no_of_items':'1',
        'price': 20000,
        'order_ID': 1011,
        'payment': 'cash on delivery',
        
    }
]

if __name__=='__main__':
    app.run(debug=True)