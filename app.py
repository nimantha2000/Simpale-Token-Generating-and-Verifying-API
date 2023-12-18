from flask import Flask, jsonify, request
from utils import generate_token, verify_token

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/generate-token', methods=['POST'])
def generate_token_route():
    data = request.json
    if not data or 'user_id' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    user_id = data['user_id']
    token = generate_token(user_id)
    return jsonify({'token': token})


@app.route('/verify-token', methods=['POST'])
def verify_token_route():
    data = request.json
    if not data or 'token' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    token = data['token']
    try:
        payload = verify_token(token)
        return jsonify({'user_id': payload['user_id']})
    except Exception as e:
        return jsonify({'error': str(e)}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0')
