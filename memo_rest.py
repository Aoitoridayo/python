from flask import Flask, jsonify, request
from memo_manager import MemoManager

app = Flask(__name__)
manager = MemoManager()

@app.route('/memo', methods=['GET', 'POST'])
def memo():
    if request.method == 'GET':
        return jsonify([memo.to_json() for memo in manager.get_all_memos()])
    else:
        title = request.json.get('title')
        content = request.json.get('content')
        memo = manager.add_memo(title, content)
        return jsonify(memo.to_json())

@app.route('/memo/<id>', methods=['GET', 'PUT', 'DELETE'])
def memo_id(id: str):
    if request.method == 'GET':
        memo = manager.get_memo(id)
        if memo is None:
            return jsonify({'error': 'Memo not found.'}), 404
        return jsonify(memo.to_json())
    elif request.method == 'PUT':
        title = request.json.get('title')
        content = request.json.get('content')
        memo = manager.get_memo(id)
        if memo is None:
            return jsonify({'error': 'Memo not found.'}), 404
        memo.title = title
        memo.content = content
        return jsonify(memo.to_json())
    else:
        memo = manager.delete_memo(id)
        if memo is None:
            return jsonify({'error': 'Memo not found.'}), 404
        return jsonify(memo.to_json())

if __name__ == '__main__':
    app.run(debug=True)
