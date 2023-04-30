from flask import Flask, jsonify, render_template, redirect, url_for

app = Flask(__name__)

products = [
  {"id": 1, "name": "Product 1", "price": 10.0},
  {"id": 2, "name": "Product 2", "price": 20.0},
  {"id": 3, "name": "Product 3", "price": 30.0},
]

@app.route("/")
def home():
  return redirect(url_for('output'))

@app.route("/products", methods=["GET"])
def get_products():
  return jsonify(products)
  
@app.route("/output")
def output():
  return render_template('output.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

