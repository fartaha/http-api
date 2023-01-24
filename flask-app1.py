from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum():
    data = request.get_json()
    a = data['a']
    b = data['b']
    result = a + b
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(port=8000)
