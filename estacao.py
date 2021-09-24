# estação meteorológica de monitoramento de temperatura e umidade no módulo ESP32 utilizando o sensor DTH11

import dht
import machine
import urequests
import time

d = dht.DHT11(machine.Pin(4))

def conecta(ssid, senha):
    import network
    import time
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, senha)
    for t in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    return station

print("Conectando...")
station = conecta("NOMEDAREDE", "SENHADAREDE")
print("Conectado!...")

if not station.isconnected():
    print("Nao conectado!...")
else:
    while True:
        d.measure()
        print("Acessando o ThingSpeak...")
        print("temp:{} Umid:{}".format(d.temperature(), d.humidity()))
        response = urequests.get("https://api.thingspeak.com/update?api_key=A4AUKK4091WTQU2R&field1={}&field2={}".format(d.temperature(), d.humidity()))
        print("Dados enviados!")
        response.close()
        time.sleep(10)







    
    
    