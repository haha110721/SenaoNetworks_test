from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from tool import validate_username, validate_password, is_account_locked

app = Flask(__name__)

accounts = {} # 用於存儲帳戶及密碼
accounts_lock = {}

@app.route("/create", methods = ['POST'])
def create_account():
    data = request.get_json() # 獲取 json 數據
    username = data.get('username')
    password = data.get('password')

    if username in accounts:
        return jsonify({'success': False, 'reason': 'Username already exists'}), 400 # Bad Request

    if not validate_username(username):
        return jsonify({'success': False, 'reason': 'Username is not valid'}), 400

    if not validate_password(password):
        return jsonify({'success': False, 'reason': 'Password is not valid'}), 400

    # 創建帳戶
    accounts[username] = password
    return jsonify({'success': True, 'reason': 'Account created successfully'}), 201 # Created

@app.route('/verify', methods = ['POST'])
def verify_account():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if is_account_locked(accounts_lock, username):
        return jsonify({'success': False, 'reason': 'Account is locked. Please try again 1 minute later'}), 423 # Locked

    if username in accounts and accounts[username] == password:
        accounts_lock.pop(username, None)
        return jsonify({'success': True, 'reason': 'Account verified successfully'}), 200 # OK
    else:
        if username in accounts_lock:
            accounts_lock[username][0] += 1
            if accounts_lock[username][0] >= 5:
                accounts_lock[username][1] = datetime.now() + timedelta(minutes = 1)
                if is_account_locked(accounts_lock, username):
                    return jsonify({'success': False, 'reason': 'Account is locked. Please try again 1 minute later'}), 423
        else:
            accounts_lock[username] = [1, None]

        return jsonify({'success': False, 'reason': 'Invalid username or password'}), 401 # Unauthorized

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0')