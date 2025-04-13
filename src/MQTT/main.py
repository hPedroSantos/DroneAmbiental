import time
from MQTT.configs.mqtt_broker_setup import mqtt_broker_configs
from MQTT.mqtt_connection.mqtt_client_connection import MqttClientConnection

def start():
    mqtt_client_connection = MqttClientConnection(
        mqtt_broker_configs["HOST"],
        mqtt_broker_configs["PORT"],
        mqtt_broker_configs["CLIENT_NAME"],
        mqtt_broker_configs["KEEPALIVE"]
    )
    mqtt_client_connection.start_connection()

    while True: 
        time.sleep(0.001)
        