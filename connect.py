#!python3
import paho.mqtt.client as mqtt
from datetime import datetime
import numpy as np
import logging


temp_list = []
time_list = []
logging.basicConfig(filename="logFile.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)


def write_to_log(cpu_usage):
    logging.info(str(cpu_usage))


def on_message(client, userdata, message):
    print("mensagem recebida: ", str(message.payload.decode("utf-8")))
    print("topico: ", message.topic)
    write_to_log(message.payload)


def on_log(client, userdata, level, buf):
    print("log: ",buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("conectou")
    else:
        print("Falha na conexão. Código retornado:", rc)


# definindo o cliente
client_name = 'iure'
client = mqtt.Client(client_name)

# definindo o acesso ao broker
broker_address = "localhost"
port = 1883
timelive = 60

# definindo as funções de callback
client.on_connect = on_connect
client.on_log = on_log
client.on_message = on_message
client.username_pw_set(username="iure", password="mosquito")

print("Conectando ao broker")
client.connect(broker_address, port, timelive)

# subscrever ao tópico de uso de cpu
client.subscribe("pc/usage")

# necessário para executar as funções de callback
client.loop_forever()


