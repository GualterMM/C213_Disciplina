import tkinter as tk
from tkinter import ttk
import tk_tools
import paho.mqtt.client as mqtt

def setup_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect

    # Connect to the Mosquitto Test Server
    client.connect("test.mosquitto.org", 1883, 60)

    # Start the MQTT client loop in a separate thread
    client.loop_start()

    return client

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def subscribe(client: mqtt.Client, topic, gauge):
    def on_message(client, userdata, msg):
        # Update the sensor reading and gauge value when a new message is received
        sensor_reading = float(msg.payload.decode())
        
        if isinstance(gauge, tk_tools.Gauge):
            gauge.set_value(sensor_reading)
        else:
            gauge.config(text=f"Setpoint Atual: {sensor_reading}")

    client.subscribe(topic)
    client.on_message = on_message

def send_number_to_topic(client, topic, entry):
    try:
        number = float(entry.get())
        client.publish(topic, str(number))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    # TKinter root
    root = tk.Tk()
    root.title("Interface para leitura de temperatura por MQTT")
    
    client1 = setup_mqtt_client()
    client2 = setup_mqtt_client()
    client3 = setup_mqtt_client()
    client4 = setup_mqtt_client()

    # Gauge for displaying temperature values
    temp_gauge = tk_tools.Gauge(root, height=120, width=250,
                                max_value=10,
                                min_value=-10,
                                label='Temperatura',
                                unit='°C',
                                divisions=10, yellow=80, red=90,
                                red_low=20, yellow_low=30, bg='lavender')
    temp_gauge.grid(row=0, column=0, sticky='news')

    # Gauge for displaying error values
    err_gauge = tk_tools.Gauge(root, height=120, width=250,
                                max_value=18,
                                min_value=-8,
                                label='Erro',
                                unit='°C',
                                divisions=10, yellow=80, red=90,
                                red_low=20, yellow_low=30, bg='lavender')
    err_gauge.grid(row=1, column=0, sticky='news')

    # Setpoint indicator
    sp_label = ttk.Label(root, text="Setpoint Atual: 0")
    sp_label.grid(row=0, column=1, sticky="news")

    # Setpoint changer
    f1 = tk.Frame(root)
    entry_label = ttk.Label(f1, text="Novo Setpoint: ")
    entry = ttk.Entry(f1)
    send_button = ttk.Button(f1, text="Alterar", command=lambda: send_number_to_topic(client4, "GMIR/Resfriador/SPnovo", entry))
    f1.grid(row=1, column=1, sticky='news')
    entry_label.pack()
    entry.pack()
    send_button.pack()

    subscribe(client1, "GMIR/Resfriador/Temperatura", temp_gauge)
    subscribe(client2, "GMIR/Resfriador/Erro", err_gauge)
    subscribe(client3, "GMIR/Resfriador/SPatual", sp_label)

    root.mainloop()

if __name__ == '__main__':
    main()