import paho.mqtt.client as mqtt
import random
import time

# --- Configurações do Broker MQTT ---
# Aponta para o broker local (Mosquitto) instalado na mesma máquina.
BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
# Tópico para enviar a contagem de pessoas.
TOPIC = "casa/sala/presenca"

# --- Lógica Principal ---
# Cria uma nova instância de cliente MQTT
try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="sensor_presenca_01")
except:
    client = mqtt.Client(client_id="sensor_presenca_01")

print("Conectando ao broker local...")
try:
    # Conecta ao broker local
    client.connect(BROKER_ADDRESS, BROKER_PORT)
except Exception as e:
    print(f"Erro ao conectar ao broker local: {e}")
    print("Verifique se o serviço Mosquitto está em execução.")
    exit()

# Inicia o loop em background para manter a conexão
client.loop_start()

print(f"Sensor de presença ativado. Publicando no tópico '{TOPIC}'.")
print("Pressione CTRL+C para sair.")

try:
    while True:
        # Gera um número aleatório entre 0 e 3 (inclusive)
        pessoas = random.randint(0, 3)
        
        # Converte o número para string para poder publicar
        mensagem = str(pessoas)

        # Publica a mensagem no tópico
        client.publish(TOPIC, mensagem)
        
        print(f"Publicado: {pessoas} pessoas na sala.")
        
        # Aguarda 3 segundos antes da próxima leitura
        time.sleep(3)

except KeyboardInterrupt:
    print("\nEncerrando o sensor de presença.")
finally:
    client.loop_stop()
    client.disconnect()
    print("Desconectado.")

