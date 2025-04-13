from MQTT.configs.mqtt_broker_setup import mqtt_broker_configs
from database.db_conn import add_database

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Me conectei {client}")
        for topic in mqtt_broker_configs["TOPIC"]:
            client.subscribe(topic)
    else:
        print(f"Deu erro {rc}")

def on_message(client, userdata, msg):
    message = {
        "topico": msg.topic,
        "conteudo": msg.payload.decode()
    }
    print(f"Mensagem recebida no tópico {msg.topic}: {msg.payload.decode()}")
    add_database(topico=message["topico"], valor=message["conteudo"])
    

def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Cliente subscribe {mqtt_broker_configs['TOPIC']}")


