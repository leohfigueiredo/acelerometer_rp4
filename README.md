# acelerometer_rp4
Sense HAT Accelerometer Monitor - AWS
# Sense HAT Accelerometer Monitor

This project uses the Sense HAT module in Raspberry Pi to monitor the position of the accelerometer and send the data to AWS IoT Core using MQTT protocol. It also displays a graphical arrow on the Sense HAT LED matrix to indicate the inclination.

## Prerequisites

- Raspberry Pi with Sense HAT module
- Python 3.x
- Paho MQTT library (`paho-mqtt`)

## Setup

1. Connect the Sense HAT module to your Raspberry Pi.
2. Install the required dependencies by running the following command:
   ```
   pip install paho-mqtt
   ```
3. Clone this repository to your Raspberry Pi.

## Usage

1. Open a terminal and navigate to the repository folder.
2. Run the following command to start the accelerometer monitor:
   ```
   python accelerometer_monitor.py
   ```
3. The program will display the accelerometer position on the terminal and send the data to AWS IoT Core.
4. The Sense HAT LED matrix will show a red arrow pointing left if the inclination is to the left, a green arrow pointing right if the inclination is to the right, or be cleared if the inclination is neutral.

## AWS IoT Core Setup

To receive the accelerometer data on AWS IoT Core, you need to set up the AWS IoT Core service and configure the necessary resources. Here are the general steps:

1. Create an AWS IoT Core Thing for your Raspberry Pi.
2. Create an AWS IoT Core MQTT topic to receive the accelerometer data.
3. Configure the necessary certificates and keys for secure communication.
4. Update the MQTT broker settings in the `accelerometer_monitor.py` file with the appropriate values.

## Customization

- You can modify the colors of the arrows by changing the RGB values in the `verde` (green) and `vermelho` (red) variables.
- The arrow patterns for left and right inclination can be customized by modifying the `seta_esquerda` (left arrow) and `seta_direita` (right arrow) lists.

Feel free to customize and adapt this code to fit your specific requirements!

## License

This project is licensed under the [MIT License](LICENSE).
