# IoT
Tarefas relacionadas a matéria de Segurança em IoT

## Configuração e execução do broker mosquitto
- Primeiramente, rode o container (sem daemon) com:
```
sudo docker-compose up 
``` 
- Posteriormente, rode entre no container com:
```
sudo docker exec -it mqtt bash
```
- Execute o seguinte comando para criar um arquivo de texto com senha para um usuário:
```
mosquitto_passwd -c file.txt <user>
```
- Copie esse arquivo txt para o diretório `/etc/mosquitto`, edite o arquivo 
`mosquiito.conf` para as seguintes configurações:
```
allow_anonymous false
password_file /etc/mosquitto/file.txt
```
- Reinicie o mosquitto com:
```
service mosquitto restart
```
