# Aplicación de Ping

Esta es una aplicación desarrollada en Python que realiza ping a una dirección IP durante un periodo de tiempo determinado y muestra estadísticas y gráficos en tiempo real. La aplicación está diseñada para facilitar el monitoreo de la conectividad de una red y analizar los tiempos de respuesta (RTT) de los paquetes de ping.

## Requerimientos

- Python 3.7 o superior.
- Los siguientes paquetes de Python deben estar instalados:
  - `ping3`
  - `matplotlib`
  - `tkinter`
  - `matplotlib.backends.backend_tkagg`

## Uso

1. Clona o descarga el repositorio de la aplicación en tu máquina local.
2. Asegúrate de tener instalados los requerimientos mencionados anteriormente.
3. Ejecuta el archivo `app.py` para iniciar la aplicación.
4. Se abrirá una ventana que muestra el formulario de la aplicación.
5. Ingresa la dirección IP que deseas hacer ping en el campo correspondiente.
6. Selecciona la duración del proceso de ping en el desplegable. Puedes elegir entre 60 segundos o ingresar un número personalizado de duración en segundos.
7. Haz clic en el botón "Iniciar" para comenzar el proceso de ping.
8. La tabla mostrará los datos de ping en tiempo real, incluyendo el timestamp y los tiempos de respuesta (RTT) de cada paquete.
9. Los gráficos se generarán y se actualizarán automáticamente a medida que se reciban los datos de ping.
10. Para detener el proceso de ping en cualquier momento, haz clic en el botón "Detener".
11. Se mostrará un cuadro de diálogo con las estadísticas finales de ping, incluyendo el total de pings exitosos y el total de fallos.
12. Puedes cerrar la aplicación haciendo clic en la "X" en la esquina superior derecha de la ventana.

¡Disfruta de la aplicación de Ping y monitorea tu conectividad de red de manera sencilla!


**README.md (English)**

# Ping Application

This is a Python application that performs ping to an IP address for a specified duration and displays real-time statistics and graphs. The application is designed to facilitate network connectivity monitoring and analyze the response times (RTT) of ping packets.

## Requirements

- Python 3.7 or higher.
- The following Python packages must be installed:
  - `ping3`
  - `matplotlib`
  - `tkinter`
  - `matplotlib.backends.backend_tkagg`

## Usage

1. Clone or download the application repository to your local machine.
2. Make sure you have installed the aforementioned requirements.
3. Run the `app.py` file to start the application.
4. A window will open displaying the application form.
5. Enter the IP address you want to ping in the corresponding field.
6. Select the duration of the ping process from the dropdown. You can choose between 60 seconds or enter a custom duration in seconds.
7. Click the "Start" button to begin the ping process.
8. The table will show real-time ping data, including the timestamp and response times (RTT) of each packet.
9. The graphs will be generated and updated automatically as the ping data is received.
10. To stop the ping process at any time, click the "Stop" button.
11. A dialog box will display the final ping statistics, including the total successful pings and total failures.
12. You can close the application by clicking the "X" in the top right corner of the window.

Enjoy the Ping Application and easily monitor your network connectivity!



