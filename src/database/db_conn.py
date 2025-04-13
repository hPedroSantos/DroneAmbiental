from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')

senha = quote_plus(password)

# Conexão temporária para criar o banco se não existir
conn = mysql.connector.connect(host="localhost", user=user, password=password)
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
cursor.close()
conn.close()


db = f"mysql+mysqlconnector://{user}:{senha}@localhost:3306/{db_name}"

engine = create_engine(db)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Sensor(Base):
    __tablename__ = "sensor_data"
    id = Column(Integer, primary_key=True, autoincrement=True)
    topico = Column(String(15), nullable=False)
    valor = Column(String(15), nullable=False)
    data = Column(DateTime, default=datetime.now)

    def __init__(self, topico, valor):
        self.topico = topico
        self.valor = valor


Base.metadata.create_all(bind=engine)

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