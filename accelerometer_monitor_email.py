from sense_hat import SenseHat
import time
import json
import paho.mqtt.client as mqtt
import ssl
import smtplib
from email.mime.text import MIMEText

# Initialize the Sense HAT
sense = SenseHat()

# Define the colors
green = (0, 255, 0)    # Green color
red = (255, 0, 0)      # Red color
black = (0, 0, 0)      # Black color

# Define the pixels for the left arrow
left_arrow = [
    black, black, black, red, black, black, black, black,
    black, black, red, red, black, black, black, black,
    black, red, red, red, black, black, black, black,
    red, red, red, red, red, red, red, red,
    red, red, red, red, red, red, red, red,
    black, red, red, red, black, black, black, black,
    black, black, red, red, black, black, black, black,
    black, black, black, red, black, black, black, black
]

# Define the pixels for the right arrow
right_arrow = [
    black, black, black, black, red, black, black, black,
    black, black, black, black, red, red, black, black,
    black, black, black, black, red, red, red, black,
    red, red, red, red, red, red, red, red,
    red, red, red, red, red, red, red, red,
    black, black, black, black, red, red, red, black,
    black, black, black, black, red, red, black, black,
    black, black, black, black, red, black, black, black
]

# Function to check the inclination and send email alert if conditions are met
def check_inclination():
    # Read the accelerometer data
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    
    if x < -0.5:
        # Display the left arrow in red
        sense.set_pixels(left_arrow)
        message = "Warning! Accelerometer position: x={}, y={}, z={}".format(x, y, z)
        send_email_alert(message)
    elif x > 0.5:
        # Display the right arrow in green
        sense.set_pixels(right_arrow)
        message = "All good! Accelerometer position: x={}, y={}, z={}".format(x, y, z)
        send_email_alert(message)
    else:
        sense.clear()  # Clear the display if the inclination is neutral

def send_email_alert(message):
    # SMTP server settings and login credentials
    smtp_server = 'your_smtp_server'  # Replace with your SMTP server
    smtp_port = 587  # Replace with the SMTP server port
    smtp_username = 'your_username'  # Replace with your login email
    smtp_password = 'your_password'  # Replace with your login password

    # Email settings
    sender_email = 'sender@example.com'  # Replace with your email address
    receiver_email = 'receiver@example.com'  # Replace with the recipient's email address
    subject = 'Accelerometer Alert'
    body = message

    # Create the MIMEText object with the email body
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Create an SMTP session and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# MQTT broker settings
mqtt_broker = "your_mqtt_broker"  # Replace with your MQTT broker address
mqtt_port = 8883
mqtt_ca_cert = './path_to_ca_certificate.pem'  # Replace with the path to your CA certificate
mqtt_client_cert = './path_to_client_certificate.pem'  # Replace with the path to your client certificate
mqtt_client_key = './path_to_client_private_key.pem'  # Replace with the path to your client private key
mqtt_topic = "your_mqtt_topic"  # Replace with your MQTT topic

# MQTT connection callback function
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker successfully!")
    else:
        print("Failed to connect to MQTT broker. Return code:", rc)

# MQTT message received callback function
def on_message(client, userdata, msg):
    print("Message received on topic:", msg.topic)
    print("Payload:", msg.payload.decode())

# Create the MQTT client object
client = mqtt.Client()

# Set the MQTT connection callback
client.on_connect = on_connect

# Set the MQTT message received callback
client.on_message = on_message

# Set up TLS/SSL for the MQTT connection
client.tls_set(ca_certs=mqtt_ca_cert, certfile=mqtt_client_cert, keyfile=mqtt_client_key, tls_version=ssl.PROTOCOL_TLS)

try:
    # Connect to the MQTT broker
    client.connect(mqtt_broker, mqtt_port, keepalive=60)

    # Subscribe to the MQTT topic
    client.subscribe(mqtt_topic)

    while True:
        # Check the inclination and publish the message to the MQTT topic
        check_inclination()

        # Read the accelerometer data
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        # Prepare the data for sending to the MQTT broker
        data = {
            'x': x,
            'y': y,
            'z': z
        }
        payload = json.dumps(data)

        # Publish the message to the MQTT topic
        client.publish(mqtt_topic, payload)

        # Wait for 1 second before checking again
        time.sleep(1)

except KeyboardInterrupt:
    # Clear the display and terminate the execution on interruption
    sense.clear()
    client.disconnect()
