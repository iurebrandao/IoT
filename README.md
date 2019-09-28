# IoT
Tarefas relacionadas a matéria de Segurança em IoT

## Configuração e execução do broker mosquitto
- Primeiramente, rode o container (sem daemon) com:
```
sudo docker-compose up 
``` 
- Posteriormente, entre no container com:
```
sudo docker exec -it mqtt bash
```
- Dentro do container, execute o seguinte comando para criar um arquivo de texto com senha para um usuário:
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
## Configuração do ELK

- Rode o comando do docker:
```
docker-compose up elk
```

- Após isso, execute o comando para entrar no container:
```
sudo docker exec -it <nome-do-container> /bin/bash
```
- Pare o LogStash com o seguinte comando:
```
/etc/init.d/logstash stop
```
- Execute o seguinte comando para pegar novos logs:
```
/opt/logstash/bin/logstash -f logstash-simple.conf
```
- No kibana, crie um `index_pattern` como: `index_name`.
- A partir disso, basta criar as visualizações no Kibana para acompanhar os logs.