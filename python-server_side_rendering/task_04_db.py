from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file():
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return []

def read_csv_file():
    try:
        products = []
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return []

def read_from_sql(id=None):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    if id:
        cursor.execute("SELECT * FROM Products WHERE id = ?", (id,))
    else:
        cursor.execute("SELECT * FROM Products")

    rows = cursor.fetchall()
    conn.close()

    products = [{"id": row[0], "name": row[1], "category":row[2], "price": row[3]} for row in rows]

    return products



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    if not source:
        return "source is a required parameter"

    id = request.args.get('id', type=int)

    if source == 'json':
        products = read_json_file()
    elif source == 'csv':
        products = read_csv_file()
    elif source == 'sql':
        products = read_from_sql()
    else:
        return "Wrong source"
    
    if id:
        products = [product for product in products if product['id'] == id]

        if not products:
            return render_template('product_display.html', error="Product not found")
        
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)