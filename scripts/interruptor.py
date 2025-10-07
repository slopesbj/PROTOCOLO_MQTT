import paho.mqtt.client as mqtt
import time

# --- Configurações do Broker MQTT ---
BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
# Tópico para controlar a lâmpada. Ex: "casa/sala/luz"
TOPIC = "casa/sala/luz"

# --- Lógica Principal ---
# Cria uma nova instância de cliente MQTT
try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="interruptor_sala")
except:

    client = mqtt.Client(client_id="interruptor_sala")

print("Conectando ao broker...")
try:
    client.connect(BROKER_ADDRESS, BROKER_PORT)
except Exception as e:
    print(f"Erro ao conectar: {e}")
    exit()

# Inicia o loop em background para manter a conexão
client.loop_start()

print("Interruptor pronto no Tópico '{TOPIC}' Pressione Enter para ligar/desligar a luz.")
print("Pressione CTRL+C para sair.")

try:
    ligada = False #o interruptor começa com desligado
    while True: #loop infinito
        # Aguarda o usuário pressionar Enter
        input() #aguardando o Enter
        
        if ligada: #Se a lampada estiver ON sera enviado OFF
            mensagem = "OFF"
            print("Enviando comando: DESLIGAR")
        else: #Se a lampada tiver OFF sera enviada ON 
            mensagem = "ON"
            print("Enviando comando: LIGAR")

        # Publica a mensagem ("ON" ou "OFF") no tópico
        client.publish(TOPIC, mensagem)
        
        # Inverte o estado da lâmpada para o retorno do loop
        ligada = not ligada

except KeyboardInterrupt:
    print("\nEncerrando o interruptor.")
finally:
    client.loop_stop()
    client.disconnect()
    print("Desconectado.")

