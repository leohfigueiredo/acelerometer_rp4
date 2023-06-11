# Sense HAT Accelerometer Monitor and Email Alert

This project uses the Sense HAT module in Raspberry Pi to monitor the position of the accelerometer, send the data to AWS IoT Core using MQTT protocol, and send email alerts based on the accelerometer readings.

## Prerequisites

- Raspberry Pi with Sense HAT module
- Python 3.x
- Paho MQTT library (`paho-mqtt`)
- `smtplib` library

## Setup

1. Connect the Sense HAT module to your Raspberry Pi.
2. Install the required dependencies by running the following command:
   ```
   pip install paho-mqtt
   pip install secure-smtplib
   ```
3. Clone this repository to your Raspberry Pi.

## Usage

1. Open a terminal and navigate to the repository folder.
2. Run the following command to start the accelerometer monitor:
   ```
   python accelerometer_monitor_email.py
   ```
3. The program will display the accelerometer position on the terminal, send the data to AWS IoT Core, and send email alerts if the conditions are met.
4. The Sense HAT LED matrix will show a red arrow pointing left if the inclination is to the left, a green arrow pointing right if the inclination is to the right, or be cleared if the inclination is neutral.
5. Check the email account configured in the script to receive the email alerts.

## AWS IoT Core Setup

To receive the accelerometer data on AWS IoT Core, you need to set up the AWS IoT Core service and configure the necessary resources. Here are the general steps:

1. Create an AWS IoT Core Thing for your Raspberry Pi.
2. Create an AWS IoT Core MQTT topic to receive the accelerometer data.
3. Configure the necessary certificates and keys for secure communication.
4. Update the MQTT broker settings in the `accelerometer_monitor_email.py` file with the appropriate values.

## Email Alert Setup

To send email alerts, you need to configure an SMTP server and provide the necessary credentials. Here are the steps:

1. Replace the SMTP server details in the `send_email_alert` function.
2. Replace the sender and recipient email addresses in the `send_email_alert` function.

## Customization

- You can modify the colors of the arrows by changing the RGB values in the `green` and `red` variables.
- The arrow patterns for left and right inclination can be customized by modifying the `left_arrow` and `right_arrow` lists.

Feel free to customize and adapt this code to fit your specific requirements!

## License

This project is licensed under the [MIT License](LICENSE).
