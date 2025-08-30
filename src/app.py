from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/moebel', methods=['GET'])
def get_moebel():
    return jsonify({'moebel': ['Sofa', 'Tisch', 'Stuhl']})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
