from flask import Flask
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

# @app.route('/myroute', methods=['GET'])
# def hello_world():
#     return '<h1>Hello!</h1>'

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete: ",position)
    return jsonify(todos)
    
todos = [ { "label": "My first task", "done": False } ]


# suppose you have your data in the variable named some_data
    # some_data = { "name": "Bobby", "lastname": "Rixer" }

# @app.route('/myroute', methods=['GET'])
# def hello_world():
#     # you can convert that variable into a json string like this
#     json_text = jsonify(some_data)

#     # and then you can return it to the front end in the response body like this
#     return json_text

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)