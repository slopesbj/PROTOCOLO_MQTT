import paho.mqtt.client as mqtt

# --- Configurações do Broker MQTT ---
# Aponta para o broker local (Mosquitto) instalado na mesma máquina.
BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
# O monitor se inscreve no mesmo tópico que o sensor publica
TOPIC = "casa/sala/presenca"

# --- Função chamada quando o cliente se conecta ao broker ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Monitor conectado ao broker local!")
        # Se inscreve no tópico para receber as mensagens
        client.subscribe(TOPIC)
        print(f"Aguardando dados no tópico: '{TOPIC}'")
    else:
        print(f"Falha na conexão, código: {rc}")

# --- Função chamada quando uma MENSAGEM é recebida ---
def on_message(client, userdata, msg):
    # Decodifica a mensagem recebida (de bytes para string)
    pessoas = msg.payload.decode()
    
    print(f"Atualização: {pessoas} pessoas na sala de jantar.")

# --- Lógica Principal ---
# Cria uma nova instância de cliente MQTT
try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id="monitor_sala_jantar_01")
except:
    client = mqtt.Client(client_id="monitor_sala_jantar_01")

# Define as funções de callback
client.on_connect = on_connect
client.on_message = on_message

# Tenta conectar ao broker
try:
    client.connect(BROKER_ADDRESS, BROKER_PORT)
except Exception as e:
    print(f"Erro ao conectar ao broker local: {e}")
    print("Verifique se o serviço Mosquitto está em execução.")
    exit()

# O loop_forever() mantém o script rodando para escutar por mensagens
# indefinidamente.
client.loop_forever()

