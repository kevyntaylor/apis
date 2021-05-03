from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='prueba_tecnica'
mysql = MySQL(app)

from products import products


@app.route('/products/<string:id>', methods=['GET'])
def getProductById(id):
    print(id)
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM products WHERE id = %s',(id))
    row_headers=[x[0] for x in cur.description] 
    data = cur.fetchall()
    json_data=[]
    for result in data:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)

@app.route('/products', methods=['POST'])
def addProduct():
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO products(name,price,quantity) VALUES (%s,%s,%s)',(request.json['name'],request.json['price'],request.json['quantity']))
    mysql.connection.commit()
    id = cur.lastrowid
    return getInfo(id)


def getInfo(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM products WHERE id = '+ str(10))
    row_headers=[x[0] for x in cur.description] 
    data = cur.fetchall()
    json_data=[]
    for result in data:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify({"message":"Product save succesfully", "product": json_data})

if __name__ == '__main__':
    app.run(debug=True, port=4000)