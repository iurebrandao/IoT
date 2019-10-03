# IoT
Tarefas relacionadas a matéria de Segurança em IoT

## Configuração e execução do broker mosquitto
- Primeiramente, rode o container (sem daemon) com:
```
sudo docker-compose up mqtt
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
- Execute o script de conectar para escrever os logs de tempetura com:
```
python3 /home/connect.py
```
- Pare o LogStash com o seguinte comando:
```
/etc/init.d/logstash stop
```
- Crie o arquivo `logstash-simple.conf` com as mesmas configurações do arquivo 
nesse repositório. Após isso, execute o seguinte comando para pegar novos logs:
```
/opt/logstash/bin/logstash -f logstash-simple.conf
```
- Verifique se o elastic pegou os arquivos de log no seguinte endereço: `http://localhost:9200/_cat/indices?v`
- No kibana, crie um `index_pattern` como: `index_name`.
- A partir disso, basta criar as visualizações no Kibana para acompanhar os logs.


## Como atualizar a imagem no docker hub
- Caso queira atualizar as imagens que foram para o docker hub e depois utilizar no GNS3, primeiro faça um commit com as mudanças:
 ```
docker commit <container_id> iurebrandao/elk-connect:1.00
```

Depois utilize o seguinte comando para ver as imagens:
```
docker images
```
- Após localizar a sua imagem, mude o nome dela para a versão que você desejar:
```
docker tag <image_id> iurebrandao/elk-python:<versao> 
```
- Faça o login no docker hub pelo terminal:
```
docker login --username=<username> 
```
- Agora basta subir para o docker hub com o comando:
```
docker push iurebrandao/elk-python:<versao>
```

## Script do client
- Para executar o script do client, primeiro execute o container:
```
docker run -it iurebrandao/python-client:1.01
```
- Agora execute com:
```
python3 client.py
```
