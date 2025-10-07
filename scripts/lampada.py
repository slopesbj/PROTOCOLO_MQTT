import paho.mqtt.client as mqtt

BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883

# A lâmpada se inscreve no mesmo tópico que o interruptor 
TOPIC = "casa/sala/luz"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Lâmpada conectada e pronta para receber comandos!")
        # Se inscreve no tópico para receber as mensagens
        client.subscribe(TOPIC)
        print(f"Aguardando comandos no tópico: '{TOPIC}'")
    else:
        print(f"Falha na conexão, código: {rc}")

def on_message(client, userdata, msg):
    # Decodifica a mensagem recebida (de bytes para string)
    comando = msg.payload.decode()
    
    print(f"\nComando recebido: '{comando}'")

    if comando == "ON":
        print("💡  Lâmpada ACESA  💡")
    elif comando == "OFF":
        print("🔌  Lâmpada APAGADA 🔌")
    else:
        print(f"(Comando '{comando}' não reconhecido)")

# Cria uma nova instância de cliente MQTT
try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id="lampada_sala_01")
except:
    client = mqtt.Client(client_id="lampada_sala_01")

# Define as funções de callback
client.on_connect = on_connect
client.on_message = on_message

# Tenta conectar ao broker
try:
    client.connect(BROKER_ADDRESS, BROKER_PORT)
except Exception as e:
    print(f"Erro ao conectar: {e}")
    exit()

# mantém o script rodando para escutar por mensagens indefinidamente.

client.loop_forever()
