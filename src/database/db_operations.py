from database.db_conn import session, Sensor

def add_database(topico, valor):
    sensor = Sensor(topico=topico, valor=valor)
    session.add(sensor)
    session.commit()

def fetch_database():
    list_sensor_data = session.query(Sensor).all()

    data = []

    for item in list_sensor_data:
        res = {
            "id": item.id,
            "topico": item.topico,
            "valor": item.valor,
            "data": item.data
        }
        data.append(res)

    session.close()

    return data