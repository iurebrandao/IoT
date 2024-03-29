#!python3
import paho.mqtt.client as mqtt
import os
import signal
import sys
import sched
import time

s = sched.scheduler(time.time, time.sleep)


#  método que retorna a utilização de cpu
def read_cpu_usage():
    return str('{:.0f}'.format(float(os.popen('cat /proc/loadavg').readline().split()[0]) / float(os.popen('nproc').readline()) * 100))


# Função de callback quando publica alguma mensagem
def on_publish(client, userdata, result):
    print("Utilização de CPU publicada: ", result)
    pass


# Finalizar o script quando o usuário apertar "Ctrl+C"
def signal_handler(sig, frame):
    print('Finalizando o script...')
    client.loop_stop()
    client.disconnect()
    sys.exit(0)


# write cpg usage to log in every minute
def publish_cpu_usage(sc, client):
    print('publicando utilização da cpu')
    client.publish("pc/usage", read_cpu_usage())
    s.enter(60, 1, publish_cpu_usage, (sc, client))


if __name__ == "__main__":
    # definindo o cliente
    client_name = 'client'
    client = mqtt.Client(client_name)

    # definindo o acesso ao broker
    broker_address = "localhost"
    port = 1883
    timelive = 60

    client.username_pw_set(username="iure", password="mosquito")
    client.connect(broker_address, port)

    client.loop_start()

    signal.signal(signal.SIGINT, signal_handler)

    s.enter(1, 1, publish_cpu_usage, (s, client))
    s.run()














