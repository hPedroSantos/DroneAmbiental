from database.db_conn import session, SensorCO, SensorQualidadeAr
from database.tableconfig import tables


def fetch_db_co():

    sensor_co_query = session.query(SensorCO).all()

    data_co = []

    for item in sensor_co_query:
        res = {
            "id": item.id,
            "topico": item.topico,
            "valor": item.valor,
            "data": item.data
        }
        data_co.append(res)

    session.close()

    return data_co

def fetch_db_qual():

    sensor_qual_query = session.query(SensorQualidadeAr).all()

    data_qual = []

    for item in sensor_qual_query:
        res = {
            "id": item.id,
            "topico": item.topico,
            "valor": item.valor,
            "data": item.data
        }
        data_qual.append(res)

    session.close()

    return data_qual