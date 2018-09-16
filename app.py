from flask import Flask, jsonify 
app=Flask(__name__)

@app.route('/')
def index():
    return jsonify({'about':'Welcome to Fast-Food-Fast API'})

if __name__=='__main__':
    app.run(debug=True)