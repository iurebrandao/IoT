#!python3
import paho.mqtt.client as mqtt
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

temp_list = []
time_list = []

def plot():
    x = np.array(time_list)
    y = np.array(temp_list)
    plt.plot(x, y)
    plt.show()


def on_message(client, userdata, message):
    print("mensagem recebida: ", str(message.payload.decode("utf-8")))
    tempo = datetime.now().strftime('%H:%M:%S')
    print("tempo: ", tempo)
    print("topico: ", message.topic)
    temp_list.append(float(message.payload))
    time_list.append(tempo)
    plot()


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
client.username_pw_set(username="iure",password="mosquito")

print("Conectando ao broker")
client.connect(broker_address, port, timelive)

# subscrever ao tópico de temperatura do pc
client.subscribe("pc/temp")

# necessário para executar as funções de callback
client.loop_forever()


