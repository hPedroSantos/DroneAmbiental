from flask import Flask, jsonify
from database.db_conn import fetch_database

app = Flask(__name__)

@app.route('/all_data', methods=['GET'])
def status():
    # Aqui garantimos que a função vai buscar dados atualizados
    payload = fetch_database()
    return jsonify(payload)

if __name__ == '__main__':
    app.run(debug=True)
