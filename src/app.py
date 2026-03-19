from flask import Flask

app = Flask(__name__)

@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/todos', methods=['GET'])
def todos_route():
    return '<h1>Hello!</h1>'







# Estas 2 lineas siempre deben estar al final de la aplicacion
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)