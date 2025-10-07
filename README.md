# PROTOCOLOS
# Simulação de Automação Residencial com MQTT e Grafana

## Projeto de Mestrado em Engenharia Elétrica - UFAM

Este repositório contém os scripts e arquivos de configuração para uma simulação de automação residencial. O objetivo é demonstrar a comunicação entre dispositivos IoT (sensor de presença e lâmpada) utilizando o protocolo MQTT. Os dados são monitorados em tempo real através de um dashboard no Grafana.

---

### Arquitetura

O sistema utiliza um broker MQTT (Mosquitto) como intermediário para a troca de mensagens entre os scripts Python.

* **`sensor.py`**: Publica a contagem de pessoas no tópico `casa/sala/presenca`.
* **`monitor.py`**: Se inscreve no tópico `casa/sala/presenca` para exibir os dados no terminal.
* **`interruptor.py`**: Publica os comandos `ON`/`OFF` no tópico `casa/sala/luz`.
* **`lampada.py`**: Se inscreve no tópico `casa/sala/luz` para simular o acionamento da lâmpada.
* **`CASA-DASHBOARD.json`**: Arquivo de configuração do painel do Grafana para visualização dos dados.

---

### Pré-requisitos

* Python 3
* Broker Mosquitto
* Grafana

---

### Configuração do Ambiente

**1. Instalar dependências Python:**
```bash
pip install paho-mqtt
```

**2. Iniciar o Broker Mosquitto:**
Certifique-se de que o serviço do Mosquitto esteja em execução na sua máquina (`localhost`).

**3. Configurar o Grafana:**
* Instale o plugin **grafana-mqtt-datasource**.
    ```bash
    grafana-cli plugins install grafana-mqtt-datasource
    ```
* Reinicie o serviço do Grafana.
* Adicione uma nova fonte de dados (Data Source) do tipo MQTT apontando para `mqtt://localhost:1883`.
* Importe o dashboard `CASA-DASHBOARD.json`.

---

### Execução

Para rodar a simulação, abra um terminal para cada um dos scripts abaixo e execute-os na seguinte ordem:

1.  **Lâmpada (Subscriber):**
    ```bash
    python scripts/lampada.py
    ```

2.  **Monitor de Presença (Subscriber):**
    ```bash
    python scripts/monitor.py
    ```

3.  **Sensor de Presença (Publisher):**
    ```bash
    python scripts/sensor.py
    ```

4.  **Interruptor (Publisher):**
    ```bash
    python scripts/interruptor.py
    ```

Após iniciar os scripts, acesse o dashboard no Grafana para visualizar os dados sendo atualizados em tempo real. Para acionar a lâmpada, pressione `Enter` no terminal do `interruptor.py`.
