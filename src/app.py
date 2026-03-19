from flask import Flask, jsonify, request

app = Flask(__name__)

# Variable global todos para guardar las tareas en una list de dictionaries
todos = [{"label": 'primera tarea', "done": False}, {"label": 'terminar el proyecto', "done": True}, {"label": 'usar postman', "done": True}]

@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/todos', methods=['GET'])
def todos_route():
    json_text = jsonify(todos)

    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    #agregamos nuestra tarea al todos list
    todos.append(request_body)

    return jsonify(todos)

#ENDPOINT y peticion para hacerle delete a los todos
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)

    # Verificacion de que esa posicion existe en la lista
    if position >= len(todos):
        print("Error: esa posicion no existe en la lista:", position)
        return jsonify({"message": "Error: esa posicion no existe en la lista"}), 404
    
    todos.pop(position)

    return jsonify(todos)


# Estas 2 lineas siempre deben estar al final de la aplicacion
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)