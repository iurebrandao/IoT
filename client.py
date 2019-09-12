#!python3
import paho.mqtt.client as mqtt

def convert_temp(temp):
    if temp > 200:
        return temp / 1000
    return temp


# método que retorna a temperatura
def read_temp():
    file = open("/sys/class/thermal/thermal_zone0/temp", "r")
    temp = int(file.read().replace("\n", ""))
    file.close()
    temp = convert_temp(temp)
    return str(temp) + " °C"


# Função de callback quando publica alguma mensagem
def on_publish(client, userdata, result):
    print("Temperatura publicada: ", result)
    pass


# definindo o cliente
client_name = 'client'
client = mqtt.Client(client_name)

# definindo o acesso ao broker
broker_address = "localhost"
port = 1883
timelive = 60


client.connect(broker_address, port)

client.loop_start()

client.publish("pc/temp", read_temp())

client.loop_stop()
client.disconnect()





