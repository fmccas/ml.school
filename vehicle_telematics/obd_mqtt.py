r"""Publicar datos del veh\xC3\xADculo en un broker MQTT."""

from __future__ import annotations

import json
import time

import obd
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_TOPIC = "car/obd"


def read_obd(connection: obd.OBD) -> dict[str, float | None]:
    """Leer valores de OBD2 y devolverlos en un diccionario."""
    data: dict[str, float | None] = {}

    rpm = connection.query(obd.commands.RPM).value
    speed = connection.query(obd.commands.SPEED).value
    coolant = connection.query(obd.commands.COOLANT_TEMP).value
    voltage = connection.query(obd.commands.ELM_VOLTAGE).value

    data["rpm"] = rpm.magnitude if rpm else None
    data["speed"] = speed.magnitude if speed else None
    if coolant:
        data["coolant_celsius"] = coolant.to("celsius").magnitude
    else:
        data["coolant_celsius"] = None
    data["voltage"] = voltage.magnitude if voltage else None

    return data


def main() -> None:
    """Conectar al OBD2 y publicar datos en un broker MQTT."""
    connection = obd.OBD()
    client = mqtt.Client()
    client.connect(MQTT_BROKER)

    try:
        while True:
            payload = json.dumps(read_obd(connection))
            client.publish(MQTT_TOPIC, payload)
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        client.disconnect()
        connection.close()


if __name__ == "__main__":
    main()
