from flask import Flask, jsonify, request
from database.db_operations import fetch_db_co, fetch_db_qual, SensorCO, SensorQualidadeAr, session

app = Flask(__name__)


@app.route('/co', methods=['GET'])
def fetch_co():
    payload_co = fetch_db_co()
    return jsonify(payload_co)

@app.route('/qual_ar', methods=['GET'])
def fetch_qual():
    payload_qual = fetch_db_qual()
    return jsonify(payload_qual)

@app.route('/data_send', methods=['POST'])
def add_db():
    try:
        data = request.get_json()

        if data["topico"] == "co":
            sensor_co = SensorCO(topico=data["topico"], valor=data["valor"])
            session.add(sensor_co)
            session.commit()

            return data
        
        elif data["topico"] == "qual_ar":
            sensor_qual_ar = SensorCO(topico=data["topico"], valor=data["valor"])
            session.add(sensor_qual_ar)
            session.commit()

            return data

    except TypeError as e:
        print(f"Error {e}")
    finally:
        session.close()

if __name__ == '__main__':
    app.run(debug=False, port=5555)

