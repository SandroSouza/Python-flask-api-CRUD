from flask import Flask, jsonify, request
from flask_mysqldb import MySQL


app = Flask(__name__)

# credenciais
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'youtube'
mysql = MySQL(app)

@app.route('/')
def not_address():
    return 'Sem endereço'

#select all
@app.route('/data', methods=['GET'])
def get_data():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM User''')
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

#select one
@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM User WHERE id = %s''', (id,))
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

#create
@app.route('/data', methods=['POST'])
def add_data():
    cursor = mysql.connection.cursor()
    request_data = request.get_json()
    nome = request_data['nome']
    email = request_data['email']
    senha = request_data['senha']
    cursor.execute('''INSERT INTO User (nome, email, senha) VALUES (%s, %s, %s)''', (nome, email, senha))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Dados adicionados com sucesso'})

#update
@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    cursor = mysql.connection.cursor()
    request_data = request.get_json()
    nome = request_data['nome']
    email = request_data['email']
    senha = request_data['senha']
    cursor.execute('''UPDATE User SET nome = %s, email = %s, senha = %s WHERE id = %s''', (nome, email, senha, id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Dados atualizados com sucesso'})

#delete
@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    cursor = mysql.connection.cursor()
    cursor.execute('''DELETE FROM User WHERE id = %s''', (id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Dado deletado com sucesso'})

if __name__ == '__app__':
    app.run(debug=True)