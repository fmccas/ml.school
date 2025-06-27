# Vehicle Telematics

Este subproyecto describe c\xC3\xB3mo conectar un microcontrolador al OBD2 de un
veh\xC3\xADculo, enviar datos a un backend propio y visualizarlos en tiempo real.

## Objetivo
Hacer que tu veh\xC3\xADculo de gasolina env\xC3\xADe datos de sensores como
velocidad, RPM, temperatura y voltaje de bater\xC3\xADa hacia un backend y que
puedas consultarlos desde tu celular o laptop.

## Infraestructura
- Microcontrolador ESP32, Raspberry Pi Pico W o Arduino con WiFi.
- Interfaz OBD2 por UART o CAN bus mediante un adaptador ELM327.
- Conectividad MQTT (WiFi o 4G si se quiere movilidad).
- Backend con Mosquitto y almacenamiento en MongoDB o InfluxDB.
- Visualizaci\xC3\xB3n en Grafana o una app propia con Streamlit o React.

## Fases
1. **Adquisici\xC3\xB3n Local**: conectar el microcontrolador al OBD2 y mostrar
   los valores en consola o un dashboard embebido.
2. **Env\xC3\xADo Remoto**: publicar los datos en un broker MQTT local y
   almacenarlos en una base de datos.
3. **Visualizaci\xC3\xB3n Remota**: consultar los datos desde el celular o
   laptop usando Grafana o una peque\xC3\xB1a aplicaci\xC3\xB3n web.
4. **Analytics y Alertas** *(opcional)*: definir umbrales de salud y notificar
   cuando se incumplan.

## Scripts
El archivo `obd_mqtt.py` es un ejemplo sencillo que publica datos le\xC3\xADdos
por OBD2 en un broker MQTT.
